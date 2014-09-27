#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_sc2castsclient
----------------------------------

Tests for `sc2castsclient` module.
"""

import unittest

from sc2castsclient import *
from pprint import pprint
from tests import *

class TestSc2CastsClient(unittest.TestCase):
    '''
    Online tests, for checking if changes on sc2casts.com breaks anything
    '''
    def setUp(self):
        pass
    def tearDown(self):
        pass

    '''
    def test_index(self):
        client = Sc2CastsClient()
        actual = client.series('recent')
        assert len(actual) > 0

    def test_top_24h(self):
        client = Sc2CastsClient()
        actual = client.series('top_24h')
        assert len(actual) > 0

    def test_top_week(self):
        client = Sc2CastsClient()
        actual = client.series('top_week')
        assert len(actual) > 0

    def test_top_month(self):
        client = Sc2CastsClient()
        actual = client.series('top_month')
        assert len(actual) > 0
    '''

    def test_top_all(self):
        client = Sc2CastsClient()
        actual = client.series('top_all')
        assert len(actual) > 0

    '''
    def test_all(self):
        client = Sc2CastsClient()
        actual = client.series('all')
        assert len(actual) > 0

    def test_series_by_path_1(self):
        client = Sc2CastsClient()
        actual = client.series_by_path('/cast14705-KT-Rolster-vs-Prime-Best-of-5-2014-Proleague-Round-1')
        #assert len(actual) > 0

        assert_cast14705(actual)
    '''

if __name__ == '__main__':
    unittest.main()
