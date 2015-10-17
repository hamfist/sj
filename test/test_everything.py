# vim:fileencoding=utf-8
import os
import sys

import sj


HERE = os.path.dirname(os.path.abspath(__file__))


def open_json(namebase):
    return open(os.path.join(HERE, '{}.json'.format(namebase)))


def test_good_json_is_good(capsys):
    with open_json('good') as stream:
        assert 0 == sj.main(['sj'], stream)

    out, err = capsys.readouterr()
    assert err.strip() == ''
    assert out.strip() == ''


def test_also_good_json_is_also_good(capsys):
    with open_json('also-good') as stream:
        assert 0 == sj.main(['sj'], stream)

    out, err = capsys.readouterr()
    assert err.strip() == ''
    assert out.strip() == ''


def test_bad_json_is_bad(capsys):
    with open_json('bad') as stream:
        assert 1 == sj.main(['sj'], stream)

    err = capsys.readouterr()[1].strip().splitlines(False)
    assert '"FizzBuzz" is not snakey!' in err
    assert '"ham.boneSoup" is not snakey!' in err
    assert '"ham.X" is not snakey!' in err
    assert '"ham.0xBEEF." is not snakey!' in err


def test_bad_json_is_bad_but_quiet(capsys):
    with open_json('bad') as stream:
        assert 1 == sj.main(['sj', '-q'], stream)

    _, err = capsys.readouterr()
    assert err.strip() == ''


def test_jsonapi_json_is_good(capsys):
    for i in range(1, 25):
        with open_json('jsonapi-{:>02}'.format(i)) as stream:
            assert 0 == sj.main(['sj'], stream)

        out, err = capsys.readouterr()
        assert err.strip() == ''
        assert out.strip() == ''
