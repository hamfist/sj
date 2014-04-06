# vim:fileencoding=utf-8
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.dirname(HERE))

import sj


def test_good_json_is_good(capsys):
    with open(os.path.join(HERE, 'good.json')) as stream:
        assert 0 == sj.main(['sj'], stream)
    out, err = capsys.readouterr()
    assert err.strip() == ''
    assert out.strip() == ''


def test_also_good_json_is_also_good(capsys):
    with open(os.path.join(HERE, 'also-good.json')) as stream:
        assert 0 == sj.main(['sj'], stream)
    out, err = capsys.readouterr()
    assert err.strip() == ''
    assert out.strip() == ''


def test_bad_json_is_bad(capsys):
    with open(os.path.join(HERE, 'bad.json')) as stream:
        assert 1 == sj.main(['sj'], stream)
    _, err = capsys.readouterr()
    assert err.strip() != ''


def test_bad_json_is_bad_but_quiet(capsys):
    with open(os.path.join(HERE, 'bad.json')) as stream:
        assert 1 == sj.main(['sj', '-q'], stream)
    _, err = capsys.readouterr()
    assert err.strip() == ''
