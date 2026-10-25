#!/usr/bin/env python3
"""Verify byte identity and inventory of preserved upstream imports."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def verify():
    errors = []
    count = 0
    manifests = sorted((ROOT / 'games').glob('*/SOURCE.json'))
    for manifest in manifests:
        data = json.loads(manifest.read_text())
        game = manifest.parent
        expected = set()
        for record in data['files']:
            relative = Path(record['path'])
            if (relative.is_absolute() or '..' in relative.parts
                    or not relative.parts or relative.parts[0] != 'upstream'):
                errors.append(str(manifest) + ': unsafe file path')
                continue
            if relative.as_posix() in expected:
                errors.append(str(manifest) + ': duplicate ' + str(relative))
            expected.add(relative.as_posix())
            source = data['sources'][record['source']]
            if not re.fullmatch(r'[0-9a-f]{40}', source['commit']):
                errors.append(str(manifest) + ': invalid pinned commit')
            path = game / relative
            if not path.is_file() or path.is_symlink():
                errors.append(str(path) + ': missing or not a regular file')
                continue
            contents = path.read_bytes()
            blob = hashlib.sha1(('blob ' + str(len(contents)) + '\0').encode()
                                + contents).hexdigest()
            if (len(contents) != record['size_bytes']
                    or hashlib.sha256(contents).hexdigest() != record['sha256']
                    or blob != record['git_blob']):
                errors.append(str(path) + ': upstream bytes changed')
            count += 1
        actual = {p.relative_to(game).as_posix()
                  for p in (game / 'upstream').rglob('*') if p.is_file()}
        if expected != actual:
            errors.append(str(manifest) + ': upstream inventory mismatch')
    if not manifests:
        errors.append('No source manifests found')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Verified {count} unchanged upstream files across {len(manifests)} games.')
    return 0


if __name__ == '__main__':
    sys.exit(verify())
