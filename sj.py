#!/usr/bin/env python
# vim:fileencoding=utf-8
"""
"""
from __future__ import print_function

import argparse
import re
import sys

import ijson

__version__ = '0.2.0'

KEY_RE = re.compile('^[a-z0-9_][\\.a-z0-9_]*[a-z0-9_]*$')


def yield_offenders(stream, matcher=KEY_RE):
    parser = ijson.parse(stream)
    for prefix, event, value in parser:
        if event != 'map_key':
            continue
        if matcher.match(value):
            continue
        yield prefix, value


def main(sysargs=sys.argv[:], stream=sys.stdin):
    parser = argparse.ArgumentParser(version=__version__)
    parser.add_argument(
        '-q', '--quiet', help='exit code only', action='store_true'
    )
    args = parser.parse_args(sysargs[1:])

    res = 0
    for prefix, value in yield_offenders(stream):
        res = 1

        if args.quiet:
            continue
        if prefix != '':
            print('"{}.{}" is not snakey!'.format(prefix, value),
                  file=sys.stderr)
        else:
            print('"{}" is not snakey!'.format(value), file=sys.stderr)

    return res


if __name__ == '__main__':
    sys.exit(main())
