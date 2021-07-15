# Python API for cvr.dev

![Tests](https://github.com/cvr-dev/cvr.dev-python/actions/workflows/test.yml/badge.svg?branch=main)

The official [cvr.dev](https://cvr.dev/) Python client library.

[cvr.dev](https://cvr.dev/) is a web service that maintains a live-updated cache of the Danish CVR
registry.

We aim to provide a much simpler and more modern API compared to
Virk/CVR's own Elastic Search solution.
Our focus is on high availability and robustness, making it as easy and
reliable as possible to retrieve data about Danish companies from the CVR
database.

## Installation

`cvr` currently requires python version 3.5 or above.

### Using pip
Make sure that you have pip installed, then run the following:

```bash
pip install cvr
```

### From source

Make sure that you have pip installed, then run the following in your
project folder:

```bash
pip install .
```

## Docs

The HTTP API is available at [docs.cvr.dev](https://docs.cvr.dev/).

## Usage

In the [examples/example.py](examples/example.py) dir there's a simple example program that verifies
that your API key works and fetches different data from the server.

```python
#!/usr/bin/env python

import cvr

client = cvr.Client(api_key='your api key')
client.test_api_key()

for virksomhed in client.cvr.virksomheder(cvr_numre=[10103940]):
    print('Found virksomhed', virksomhed.cvr_nummer)

for penhed in client.cvr.produktionsenheder(p_numre=[1003388394]):
    print('Found penhed', penhed.p_nummer)
```

## Test

This project has two types of tests: live tests and local tests. The live tests
are run against our live servers and require that you set a valid API key in
the environment variable CVR_DEV_TEST_API_KEY. Note: the live tests will count
towards your usage.

We use the `unittest` module for testing. You should use the following to run
the tests:

```bash

# Run simple tests
$ python -m unittest

# Also all tests
$ CVR_DEV_TEST_API_KEY="your key" python -m unittest
```

## Alternatives

We want you to have the best experience possible; if for some reason didn't find
what you were looking for at cvr.dev, reach out to us at kontakt@cvr.dev.

If you just want to check out the market, these are potential alternatives:

- [Virk's official integration](https://datacvr.virk.dk/data/cvr-hj%C3%A6lp/indgange-til-cvr/system-til-system-adgang)
- [cvrapi.dk](https://cvrapi.dk)
- [risika.dk](https://risika.dk)
- [roaring.io](https://www.roaring.io/)
- [eanapi.dk](https://eanapi.dk)
