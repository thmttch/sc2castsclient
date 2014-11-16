#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_s2castsparser
----------------------------------

Tests for `sc2castsparser` module.
"""

import unittest

from sc2castsclient import *
from assertions import *

# the actual page for a series, where the videos are embedded
class TestSeries(unittest.TestCase):
    def setUp(self):
        self.parser = Sc2CastsParser()
    def get_test(self, name):
        with open('tests/data/' + name, 'r') as f:
            return f.read()
    def tearDown(self):
        pass

    def test_bo3_in_1_game(self):
        actual = self.parser._parse_series_page(self.get_test(
            'cast14719-Soulkey-vs-Cure-BO3-in-1-video-IEM-Cologne-2014-Korean-Qualifier'
        ))
        assert_cast14719(actual)

    # games 4 and 5 not played
    def test_5_games_4_5_not_played(self):
        actual = self.parser._parse_series_page(self.get_test(
            'cast14705-KT-Rolster-vs-Prime-Best-of-5-2014-Proleague-Round-1'
        ))
        assert_cast14705(actual)

    def test_5_games_all_played(self):
        actual = self.parser._parse_series_page(self.get_test(
            'cast14802-Innovation-vs-MC-Best-of-5-Warer.com-Invitational-Semi-Finals'
        ))
        assert_cast14802(actual)

    def test_7_games_last_3_not_played(self):
        actual = self.parser._parse_series_page(self.get_test(
            'cast14875-san-vs-Dear-Best-of-7-ASUS-ROG-Winter-2014-Finals'
        ))
        assert_cast14875(actual)

class TestIndex(unittest.TestCase):
    def setUp(self):
        # TODO test multiple pages
        self.parser = Sc2CastsParser()
    def tearDown(self):
        pass
    def loadTest(self, date_string):
        with open('tests/data/index_{}.php'.format(date_string), 'r') as f:
            test_data = f.read()
        return test_data

    def test_index_20140925(self):
        actual = self.parser._parse_index(self.loadTest('20140925'))

        expected = 21
        assert len(actual) == expected, 'Expected {0}, got {1}'.format(expected, len(actual))

        assert_cast16700(actual[0])

    def test_index_20141116(self):
        actual = self.parser._parse_index(self.loadTest('20141116'))

        expected = 21
        assert len(actual) == expected, 'Expected {0}, got {1}'.format(expected, len(actual))

        assert_cast17091(actual[0])

class TestAll(unittest.TestCase):
    def setUp(self):
        '''
        with open('tests/data/all', 'r') as f:
            self.test_html = f.read()
        '''
        # TODO test multiple pages
        self.parser = Sc2CastsParser()
    def tearDown(self):
        pass
    def loadTest(self, date_string):
        with open('tests/data/all_{}'.format(date_string), 'r') as f:
            test_data = f.read()
        return test_data

    def test_all_general(self):
        actual = self.parser._parse_all(self.loadTest('20140925'))

        expected = 100
        assert len(actual) == expected, 'Expected {0}, got {1}'.format(expected, len(actual))

    def test_all_1v1_20140925(self):
        actual = self.parser._parse_all(self.loadTest('20140925'))
        assert_cast16698(actual[2])

    def test_all_team_game_20140925(self):
        actual = self.parser._parse_all(self.loadTest('20140925'))
        assert_cast16700(actual[0])

    def test_all_1v1_20141116(self):
        actual = self.parser._parse_all(self.loadTest('20141116'))
        assert_cast17089(actual[2])

    def test_all_team_game_20141116(self):
        actual = self.parser._parse_all(self.loadTest('20141116'))
        assert_cast17091(actual[0])

class TestTop(unittest.TestCase):
    def setUp(self):
        self.parser = Sc2CastsParser()
    def tearDown(self):
        pass

    def test_top(self):
        with open('tests/data/top', 'r') as f:
            self.test_html = f.read()
        actual = self.parser._parse_top(self.test_html)

        expected = 20
        assert len(actual) == expected, 'Expected {0}, got {1}'.format(expected, len(actual))

        # check some in detail
        assert_cast16691(actual[0])

    def test_top_month(self):
        with open('tests/data/top?month', 'r') as f:
            self.test_html = f.read()
        actual = self.parser._parse_top(self.test_html)

        expected = 20
        assert len(actual) == expected, 'Expected {0}, got {1}'.format(expected, len(actual))

        # check some in detail
        assert_cast16666(actual[0])

class TestBrowse(unittest.TestCase):
    def setUp(self):
        with open('tests/data/browse', 'r') as f:
            self.test_html = f.read()
        self.parser = Sc2CastsParser()

    def test_casters(self):
        actual = self.parser.casters(self.test_html)

        expected = 763
        assert len(actual) == expected, 'Expected {0}, got {1}'.format(expected, len(actual))

    def test_events(self):
        actual = self.parser.events(self.test_html)

        #expected = 605
        expected = 607
        assert len(actual) == expected, 'Expected {0}, got {1}'.format(expected, len(actual))

    def test_matchups(self):
        actual = self.parser.matchups(self.test_html)

        expected = 6
        assert len(actual) == expected, 'Expected {0}, got {1}'.format(expected, len(actual))

    def test_players(self):
        actual = self.parser.players(self.test_html)

        expected = 108
        assert len(actual) == expected, 'Expected {0}, got {1}'.format(expected, len(actual))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
