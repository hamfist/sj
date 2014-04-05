# vim:fileencoding=utf-8
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.dirname(HERE))

import sj


class Everything(unittest.TestCase):

    def test_good_json_is_good(self):
        with open(os.path.join(HERE, 'good.json')) as stream:
            assert 0 == sj.main([], stream)

    def test_bad_json_is_bad(self):
        with open(os.path.join(HERE, 'bad.json')) as stream:
            assert 1 == sj.main([], stream)


if __name__ == '__main__':
    unittest.main()
