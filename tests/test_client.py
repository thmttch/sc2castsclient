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

    def test_all(self):
        client = Sc2CastsClient()
        actual = client.series('all')
        assert len(actual) > 0

    def test_series_by_path_1(self):
        client = Sc2CastsClient()
        actual = client.series_by_path('/cast14705-KT-Rolster-vs-Prime-Best-of-5-2014-Proleague-Round-1')

        assert_cast14705(actual)

    def test_series_by_path_2(self):
        client = Sc2CastsClient()
        actual = client.series_by_path('/cast14719-Soulkey-vs-Cure-BO3-in-1-video-IEM-Cologne-2014-Korean-Qualifier')

        assert_cast14719(actual)

    def test_series_by_path_3(self):
        client = Sc2CastsClient()
        actual = client.series_by_path('/cast14802-Innovation-vs-MC-Best-of-5-Warer.com-Invitational-Semi-Finals')

        assert_cast14802(actual)

    def test_series_by_path_4(self):
        client = Sc2CastsClient()
        actual = client.series_by_path('/cast14875-san-vs-Dear-Best-of-7-ASUS-ROG-Winter-2014-Finals')

        assert_cast14875(actual)

if __name__ == '__main__':
    unittest.main()
