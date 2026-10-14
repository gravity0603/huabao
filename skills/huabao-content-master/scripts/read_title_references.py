#!/usr/bin/env python3
"""Read category title CSVs without losing duplicate heading columns."""
import argparse
import csv
import io
import json
from pathlib import Path
import sys

FILES = {
    '旅行': ['旅行类标题参考.csv', '旅行风光.csv'],
    '萌宠': ['动物 萌宠.csv'], '动物': ['动物 萌宠.csv'],
    '明星': ['明星.csv', '明星类标题参考.csv'],
    '影视': ['影视.csv'], '动漫': ['动漫.csv'], '科技': ['科技.csv'],
    '座驾': ['座驾.csv'], '体育': ['体育.csv'], '艺术': ['艺术.csv'],
    '历史': ['艺术.csv'], '插画': ['插画.csv'], '生活': ['插画.csv'],
}


def read_file(path):
    raw = path.read_bytes()
    for encoding in ('utf-8-sig', 'gb18030'):
        try:
            decoded = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError(f'无法识别编码：{path}')
    rows = list(csv.reader(io.StringIO(decoded)))
    if not rows:
        raise ValueError(f'空CSV：{path}')
    heads = rows[0]
    cols = [i for i, h in enumerate(heads) if '标题' in h and '副' not in h]
    subs = [i for i, h in enumerate(heads) if '副标题' in h]
    if not cols:
        raise ValueError(f'未找到标题列：{path}')
    records = []
    for rownum, row in enumerate(rows[1:], 2):
        for col in cols:
            if col >= len(row) or not row[col].strip():
                continue
            # A second standalone title pool never inherits the first title's subtitle.
            subtitle = row[subs[0]].strip() if col == cols[0] and subs and subs[0] < len(row) else None
            records.append({'row': rownum, 'column': col + 1, 'title': row[col].strip(), 'subtitle': subtitle})
    return {'file': str(path), 'encoding': encoding, 'records': len(rows) - 1, 'title_count': len(records), 'title_columns': [c + 1 for c in cols], 'titles': records}


def main():
    parser = argparse.ArgumentParser(description='读取指定品类标题与副标题，优先原目录；参考样本不等于事实证据。')
    parser.add_argument('--category', choices=sorted(FILES), required=True)
    parser.add_argument('--root', default='D:/yiyouliao working/选题参考')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    original = Path(args.root)
    fallback = Path(__file__).resolve().parents[1] / 'references' / 'title-samples'
    results = []
    try:
        for filename in FILES[args.category]:
            path = original / filename
            snapshot = not path.is_file()
            if snapshot:
                path = fallback / filename
                print(f'原文件不可用，使用随包快照：{filename}；日期见manifest.json', file=sys.stderr)
            result = read_file(path)
            result['snapshot'] = snapshot
            results.append(result)
    except (OSError, ValueError, csv.Error) as exc:
        print(f'读取失败：{exc}', file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps({'category': args.category, 'reference_only': True, 'files': results}, ensure_ascii=False, indent=2))
    else:
        for result in results:
            print(f"{result['file']} | {result['title_count']}条标题表达 | {result['encoding']}")
            for record in result['titles']:
                print(f"行{record['row']} 列{record['column']} | {record['title']} | {record['subtitle'] or ''}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
