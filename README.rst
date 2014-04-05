sj
==

Enforcer of snakey JSON.

Installation
------------

With pip::

    pip install sj


With curl (separate install of ``ijson`` required)::

    curl -sLO https://raw.githubusercontent.com/snakeyjson/sj/master/sj.py
    mv sj.py ~/bin/sj
    chmod +x ~/bin/sj


Usage
-----

With whatever stdin::

    sj < some-file.json


With curl::

    curl -s http://example.org/some/path | sj
