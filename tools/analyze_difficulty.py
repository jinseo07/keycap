#!/usr/bin/env python3
"""Analyze legal key paths under an optimistic, finger-handoff-friendly model.

This uses an ANSI QWERTY left/right split. Every held key may be reassigned to
another finger between events at zero cost. The hand-capacity result assumes
one finger per depressed key and five fingers per hand; it does not model hand
geometry, one finger holding multiple keys, fatigue, or keyboard rollover.
It cannot prove that a player will cross their hands or measure real effort.
"""
import json
from pathlib import Path
import re

LEFT = frozenset('QWERTASDFGZXCVB')
RIGHT = frozenset('YUIOPHJKLNM;,./')
PATTERN = re.compile(r'\{title:"([^"\n]+)"[^\n]*?start:(\[[^\]]*\]),goal:(\[[^\]]*\]),sequence:(\[[^\]]*\])')


def load_levels():
    text = (Path(__file__).resolve().parent.parent / 'index.html').read_text(encoding='utf-8')
    levels = [(title, json.loads(start), json.loads(goal), json.loads(seq))
              for title, start, goal, seq in PATTERN.findall(text)]
    if len(levels) != 5:
        raise ValueError(f'Expected 5 stages, found {len(levels)}')
    return levels


def analyze(start, goal, sequence):
    if len(start) != len(set(start)) or len(goal) != len(set(goal)) or len(goal) != len(start):
        raise ValueError('Each stage must have equal-sized, unique start and goal sets')
    goal = frozenset(goal)
    # Key states contain no finger identity: reassigning any held key to another
    # finger is always permitted, with no assumed cost or required key release.
    paths = [(frozenset(start), ())]
    for index, key in enumerate(sequence):
        remaining = sequence[index + 1:]
        updated = []
        for held, overlaps in paths:
            if key in held:
                continue
            overlap = held | {key}
            unknown = overlap - LEFT - RIGHT
            if unknown:
                raise ValueError(f'Unsupported keys: {sorted(unknown)}')
            for released in held:
                after = overlap - {released}
                if any(k not in after and k not in remaining for k in goal):
                    continue
                if remaining and remaining[0] in after:
                    continue
                if not remaining and after != goal:
                    continue
                updated.append((after, overlaps + (overlap,)))
        paths = updated
    if not paths:
        raise ValueError('No valid path reaches the goal')
    def home_side_assistance(chord):
        return max(0, len(chord & LEFT) - 5) + max(0, len(chord & RIGHT) - 5)
    easiest_bound = min(max(map(home_side_assistance, overlaps)) for _, overlaps in paths)
    common = set(paths[0][1])
    for _, overlaps in paths[1:]:
        common.intersection_update(overlaps)
    return len(paths), easiest_bound, sorted(common, key=lambda x: (len(x), sorted(x)))


def main():
    print('ANSI QWERTY left/right split; held keys may change fingers freely between events.')
    print('Hand-capacity estimate assumes 5 fingers per hand and 1 key per finger.')
    print('A finger pressing multiple keys, reach, comfort, crossing and rollover are not measured.')
    for stage, (title, start, goal, seq) in enumerate(load_levels(), 1):
        count, bound, forced = analyze(start, goal, seq)
        formatted = ' / '.join('+'.join(sorted(chord)) for chord in forced) or 'none'
        print(f'{stage}. {title}: held={len(start)}, peak={len(start)+1}, '
              f'valid_release_paths={count}, min_opposite_home_side_keys={bound}, forced_overlaps={formatted}')


if __name__ == '__main__':
    main()
