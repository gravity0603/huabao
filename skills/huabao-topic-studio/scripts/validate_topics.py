"""Mechanical checks only; no claims about source truth, rights or semantic dedup."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


def validate(data):
    errors = []
    topics = data.get('topics') if isinstance(data, dict) else None
    if not isinstance(topics, list) or not topics:
        return ['topics must be a nonempty list']
    seen = set()
    for n, t in enumerate(topics, 1):
        prefix = f'topic {n}: '
        def fail(message):
            errors.append(prefix + message)
        if not isinstance(t, dict):
            fail('must be an object')
            continue
        for key in ('category', 'title', 'subtitle', 'summary', 'concept_key', 'status'):
            if not isinstance(t.get(key), str) or not t[key].strip():
                fail(f'{key} is required')
        category = t.get('category', '')
        title = t.get('title', '')
        subtitle = t.get('subtitle', '')
        summary = t.get('summary', '')
        limit = 7 if category in ('旅行', '旅行风光', '萌宠') else 10
        if isinstance(title, str) and len(title) > limit:
            fail(f'title exceeds {limit} characters (punctuation/spaces included)')
        if isinstance(subtitle, str) and len(subtitle) > 25:
            fail('subtitle exceeds 25 characters')
        if isinstance(summary, str) and ('\n' in summary.strip() or '\r' in summary.strip()):
            fail('summary must be one paragraph')
        if category == '萌宠' and isinstance(title, str) and title.startswith('它'):
            fail('pet title has vague subject')
        key = t.get('concept_key')
        if isinstance(key, str) and key.strip():
            if key in seen:
                fail('duplicate concept_key')
            seen.add(key)
        sources = t.get('sources')
        source_ids = set()
        opened_ids = set()
        if not isinstance(sources, list) or not sources:
            fail('sources required')
            sources = []
        for s in sources:
            if not isinstance(s, dict):
                fail('source must be an object')
                continue
            for k in ('id', 'name', 'article_title', 'url'):
                if not isinstance(s.get(k), str) or not s[k].strip():
                    fail(f'source {k} required')
            sid = s.get('id')
            if isinstance(sid, str) and sid.strip():
                if sid in source_ids:
                    fail('duplicate source id')
                source_ids.add(sid)
                if s.get('opened') is True:
                    opened_ids.add(sid)
            url = s.get('url', '')
            p = urlparse(url) if isinstance(url, str) else urlparse('')
            if p.scheme not in ('http', 'https') or not p.hostname:
                fail('source URL must be http(s) with host')
            elif p.hostname in ('example.org', 'example.com', 'example.net'):
                fail('example domain cannot be a real source')
        claims = t.get('claims')
        if not isinstance(claims, list) or not claims:
            fail('at least one source-mapped claim required')
            claims = []
        cases = t.get('cases', [])
        if not isinstance(cases, list):
            fail('cases must be a list')
            cases = []
        if category == '明星' and t.get('mode') != '单人专题':
            objects = {c.get('object') for c in cases if isinstance(c, dict) and isinstance(c.get('object'), str) and c['object'].strip()}
            if len(objects) < 4:
                fail('star collection needs at least four distinct case objects')
        for item in claims + cases:
            if not isinstance(item, dict):
                fail('claim/case must be an object')
                continue
            if not isinstance(item.get('fact'), str) or not item['fact'].strip():
                fail('claim/case fact required')
            ids = item.get('source_ids')
            if not isinstance(ids, list) or not ids or any(not isinstance(i, str) or i not in source_ids for i in ids):
                fail('claim/case needs existing source_ids')
            elif not set(ids).intersection(opened_ids):
                fail('claim/case needs at least one opened source')
            if item in cases and not item.get('object'):
                fail('case object required')
        status = t.get('status')
        if status not in ('待验证', '待补R复核', '待排期草案', '已完成选题核验'):
            fail('unknown or overstated status')
        if not isinstance(t.get('missing_checks'), list):
            fail('missing_checks list required')
        checks = t.get('checks')
        required = ('facts', 'image', 'rights', 'dedup', 'timeliness', 'category_risk', 'policy')
        if not isinstance(checks, dict):
            fail('checks object required')
        else:
            if any(type(checks.get(k)) is not bool for k in required):
                fail('all seven checks must be explicit booleans')
            if status == '已完成选题核验' and (any(checks.get(k) is not True for k in required) or t.get('missing_checks')):
                fail('completed status conflicts with missing/failed checks')
            if any(checks.get(k) is not True for k in required) and not t.get('missing_checks'):
                fail('incomplete checks need explicit missing_checks')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.path.read_text(encoding='utf-8-sig'))
        errors = validate(data)
    except (OSError, ValueError) as exc:
        print(f'Cannot read JSON: {exc}')
        return 2
    print(json.dumps({'ok': not errors, 'errors': errors, 'scope': 'mechanical only'}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
