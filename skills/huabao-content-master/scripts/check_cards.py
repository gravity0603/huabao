#!/usr/bin/env python3
"""Read-only structural checks; does not verify facts, style, or images."""
import argparse
import json
import sys
from urllib.parse import urlparse


def check(data):
    errors = []
    if not isinstance(data, dict) or not isinstance(data.get('topics'), list) or not data['topics']:
        return ['根对象需要非空topics数组']
    seen = set()
    for i, card in enumerate(data['topics'], 1):
        tag = f'第{i}题'
        if not isinstance(card, dict):
            errors.append(f'{tag}必须是对象')
            continue
        for key in ('category', 'object', 'title', 'subtitle', 'summary', 'concept_key'):
            if not isinstance(card.get(key), str) or not card[key].strip():
                errors.append(f'{tag}缺少非空字符串{key}')
        short = card.get('category') in ('旅行', '旅行风光', '萌宠', '猫狗', '熊猫')
        for key, limit in (('title', 7 if short else 10), ('subtitle', 25)):
            value = card.get(key)
            if isinstance(value, str) and len(value) > limit:
                errors.append(f'{tag}{key}超过{limit}字符')
        summary = card.get('summary')
        if isinstance(summary, str) and ('\n' in summary or '\r' in summary):
            errors.append(f'{tag}summary应为一个自然段')
        concept = card.get('concept_key')
        if isinstance(concept, str) and concept.strip():
            concept = concept.strip()
            if concept in seen:
                errors.append(f'{tag}概念键与本批前题完全相同')
            seen.add(concept)
        sources = card.get('sources')
        ids = set()
        if not isinstance(sources, list) or not sources:
            errors.append(f'{tag}需要非空sources数组')
            sources = []
        for source in sources:
            if not isinstance(source, dict):
                errors.append(f'{tag}source必须是对象')
                continue
            for key in ('id', 'name', 'article_title', 'url'):
                if not isinstance(source.get(key), str) or not source[key].strip():
                    errors.append(f'{tag}source缺少{key}')
            sid = source.get('id')
            if isinstance(sid, str) and sid.strip():
                if sid in ids:
                    errors.append(f'{tag}source id重复')
                ids.add(sid)
            url = source.get('url')
            if isinstance(url, str):
                try:
                    parsed = urlparse(url)
                    host = parsed.hostname or ''
                    reserved = ('example.com', 'example.org', 'example.net', 'localhost')
                    blocked = any(host == h or host.endswith('.' + h) for h in reserved)
                    if parsed.scheme != 'https' or not host or blocked or not parsed.path.strip('/') or any(c.isspace() for c in url):
                        errors.append(f'{tag}source URL应为非占位HTTPS正文地址')
                except ValueError:
                    errors.append(f'{tag}source URL格式无效')
            if source.get('opened') is not True:
                errors.append(f'{tag}source未记录已打开正文')
        claims = card.get('claims')
        if not isinstance(claims, list) or not claims:
            errors.append(f'{tag}需要非空claims数组')
            claims = []
        for claim in claims:
            if not isinstance(claim, dict) or not isinstance(claim.get('fact'), str) or not claim['fact'].strip():
                errors.append(f'{tag}claim缺少具体fact')
                continue
            refs = claim.get('source_ids')
            if not isinstance(refs, list) or not refs or any(not isinstance(ref, str) or ref not in ids for ref in refs):
                errors.append(f'{tag}claim需要映射到本题已有source id')
    return errors


def main():
    parser = argparse.ArgumentParser(description='只检查题卡结构、字符和来源映射；不审核图片，也不证明标题质量或事实真实性。')
    parser.add_argument('input', nargs='?', help='题卡JSON路径')
    parser.add_argument('--explain', action='store_true', help='解释检查范围')
    parser.add_argument('--dry-run', action='store_true', help='只读检查，不写文件（默认同样只读）')
    parser.add_argument('--json', action='store_true', help='输出JSON诊断')
    args = parser.parse_args()
    if args.explain:
        print('依据references/output.md：字段、7/10/25字符、单段摘要、来源记录与主张映射、完全相同概念键。')
        print('网感、吸睛、信息密度、事实与真实对象一致性、疑问语气、语义重复需编辑判断。图片由用户人工复核。')
        return 0
    if not args.input:
        parser.error('需要JSON路径，或使用--help/--explain')
    try:
        with open(args.input, encoding='utf-8-sig') as handle:
            errors = check(json.load(handle))
    except (OSError, ValueError) as exc:
        errors = [f'无法读取JSON：{exc}']
    result = {'structural_ok': not errors, 'errors': errors, 'scope': '结构检查，不证明事实、标题审美、图片或发布条件'}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print('结构检查通过；仍需编辑判断事实与标题质量。' if not errors else '\n'.join(errors))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
