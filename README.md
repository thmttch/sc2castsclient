# sc2casts client

[![PyPi Package](https://badge.fury.io/py/sc2castsclient.png)](http://badge.fury.io/py/sc2castsclient)
[![Build Status](https://travis-ci.org/thmttch/sc2castsclient.png?branch=master)](https://travis-ci.org/thmttch/sc2castsclient)
[![Downloads](https://pypip.in/d/sc2castsclient/badge.png)](https://crate.io/packages/sc2castsclient?version=latest)

Python embeddable client for crawling sc2casts.com.

* Free software: BSD license
* Documentation: http://sc2castsclient.rtfd.org.

This thing needs a lot of work.

Features
--------

```python
from sc2castsclient import *
```

Usage
--------

Set what the Makefile provides:

```bash
$> make help
```

Run tests:

```bash
# quick dev testing
$> make test

# full testing
$> make testall

coverage run --source=sc2castsclient setup.py test
coverage report -m
```

Development
--------

There is a [`download script`](tests/data/download.sh) for updating the local
test suite, for keeping up-to-date as [sc2casts.com](https://sc2casts.com)
changes over time. Note that the script is meant to be run in the same dir:

```bash
$> cd tests/data && ./download.sh
```

Release
--------

1. Open pull request, and make sure CI passes
1. `make test && make release`
1. Tag the release in github
1. Bump version so master is development
  1. `setup.py`
  1. `HISTORY.rst`

Misc
--------

Packaged with the help of https://github.com/audreyr/cookiecutter-pypackage
