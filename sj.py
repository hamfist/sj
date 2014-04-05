#!/usr/bin/env python
"""
"""
from __future__ import print_function

__version__ = '0.1.0'

import ijson

import re
import sys

KEY_RE = re.compile('^[a-z][a-z0-9_]*$')

def main():
    res = 0
    parser = ijson.parse(sys.stdin)
    for prefix, event, value in parser:
        if event != 'map_key':
            continue
        if KEY_RE.match(value):
            continue
        if prefix != '':
            print('"{}.{}" is not snakey!'.format(prefix, value),
                  file=sys.stderr)
        else:
            print('"{}" is not snakey!'.format(value), file=sys.stderr)
        res = 1
    return res


if __name__ == '__main__':
    sys.exit(main())
