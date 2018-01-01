sj
==

.. image:: https://travis-ci.org/hamfist/sj.png?branch=master
    :target: https://travis-ci.org/hamfist/sj

.. image:: https://badge.fury.io/py/sj.png
    :target: http://badge.fury.io/py/sj

Enforcer of snakey JSON.

Installation
------------

With pip::

    pip install sj


With curl (separate install of ``ijson`` required)::

    curl -sLO https://raw.githubusercontent.com/hamfist/sj/master/sj.py
    mv sj.py ~/bin/sj
    chmod +x ~/bin/sj


Usage
-----

With whatever stdin::

    sj < some-file.json


With curl::

    curl -s http://example.org/some/path | sj
