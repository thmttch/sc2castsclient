# sc2casts client

[![PyPi Package](https://badge.fury.io/py/sc2castsclient.png)](http://badge.fury.io/py/sc2castsclient)
[![Build Status](https://travis-ci.org/thmttch/sc2castsclient.png?branch=master)](https://travis-ci.org/thmttch/sc2castsclient)
[![Downloads](https://pypip.in/d/sc2castsclient/badge.png)](https://crate.io/packages/sc2castsclient?version=latest)

Python client for crawling <http://sc2casts.com>.

* Free software: BSD license
* Documentation: http://sc2castsclient.rtfd.org

# Quickstart

```python
# from example.py; assumes you have virtualenv setup or required dependencies installed

from sc2castsclient import *

if __name__ == '__main__':
    client = Sc2CastsClient()

    print('Current series on sc2casts.com main page:\n')

    for series in client.series():
        print(series.name)
```

# API

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

# Development

## Tests and reports

``` bash
# run tests
$> 

# run one test

# generate test coverage reports
$> coverage run --source=sc2castsclient setup.py test
# quick summary
$> coverage report -m
# html report
$> coverage html && open htmlcov/index.html
```

## Updating test suite

[sc2casts.com](https://sc2casts.com) is very much a live site, and so there are
occassional changes that will break this client. To make this easy, there is a
[`download script`](tests/data/download.sh) for updating the local test suite.

Note that the script is meant to be run in the same dir:

```bash
$> pushd tests/data; ./download.sh; popd
```

## Build and release

1. Open pull request, and make sure CI passes
1. `make test && make release`
1. Tag the release in github
1. Bump version so master is development
  1. `setup.py`
  1. `HISTORY.rst`

```bash
$> python setup.py dist?
```

# Issues and contributing

This project uses [Github Issues] for tracking bugs, feature requests, etc.

1. Open pull request, and make sure CI passes
1. `make test && make release`
1. Tag the release in github
1. Bump version so master is development
  1. `setup.py`
  1. `HISTORY.rst`

# Misc

Initial project template using
<https://github.com/audreyr/cookiecutter-pypackage>, heavily modified.
