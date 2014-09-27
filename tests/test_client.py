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

    def test_series_by_path(self):
        client = Sc2CastsClient()

        for path, asserter in [
            ('/cast14705-KT-Rolster-vs-Prime-Best-of-5-2014-Proleague-Round-1', assert_cast14705),
            ('/cast14719-Soulkey-vs-Cure-BO3-in-1-video-IEM-Cologne-2014-Korean-Qualifier', assert_cast14719),
            ('/cast14802-Innovation-vs-MC-Best-of-5-Warer.com-Invitational-Semi-Finals', assert_cast14802),
            ('/cast14875-san-vs-Dear-Best-of-7-ASUS-ROG-Winter-2014-Finals', assert_cast14875),
            #('/cast16666-Scarlett-vs-PartinG-Best-of-3-Red-Bull-Battle-Grounds:-Washington-Group-Stage', assert_cast16666),
            #('/cast16691-MC-vs-Dayshi-Best-of-3-All-in-1-video-2014-WCS-Europe-S3-Group-Stage-2', assert_cast16691),
            #('/cast16699-Grubby-vs-Ryung-Best-of-3-DreamHack-Stockholm-2014-Group-Stage-3', assert_cast16698),
            #('/cast16700-WelMu-vs-Ryung-Best-of-3-DreamHack-Stockholm-2014-Group-Stage-3', assert_cast16700),
        ]:
            #actual = client.series_by_path()
            #assert_cast14705(actual)
            asserter(client.series_by_path(path))

if __name__ == '__main__':
    unittest.main()
