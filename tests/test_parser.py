#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_s2castsparser
----------------------------------

Tests for `sc2castsparser` module.
"""

import unittest

from sc2castsclient import *

# the actual page for a series, where the videos are embedded
class TestSeries(unittest.TestCase):
    def setUp(self):
        self.parser = Sc2CastsParser()
    def get_test(self, name):
        with open('tests/data/' + name, 'r') as f:
            return f.read()

    def test_bo3_in_1_game(self):
        actual = self.parser._parse_series_page(self.get_test('cast14719-Soulkey-vs-Cure-Best-of-3-All-in-1-video-IEM-Cologne-2014-Korean-Qualifier'))

        a = actual
        assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

        assert a.name == 'Soulkey vs Cure (Best of 3 - All in 1 video)', a.name
        # can't get this. huh.
        assert a.path == None, a.path

        assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
        assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
        assert a.players_desc == None

        assert a.best_of == 3, a.best_of
        assert a.num_videos == 1, a.num_videos

        assert a.event.name == 'IEM Cologne 2014', a.event.name
        assert a.event_round == 'Korean Qualifier', a.event_round

        assert len(a.casters) == 1, len(a.casters)
        assert a.casters_desc == None, a.casters_desc

        assert a.cast_date == 'Jan 24, 2014', a.cast_date

        assert a.score_up == 27, a.score_up
        assert a.score_down == 2, a.score_down

        # the casts themselves
        assert len(a.casts) == a.num_videos, len(a.casts)
        # check a cast
        aa = a.casts[0]
        assert aa.__class__.__name__ == 'Sc2CastsCast', aa.__class__.__name__

        assert aa.name == 'Game 1', aa.name
        assert aa.source == 'YouTube', aa.source
        assert aa.video_url == 'https://www.youtube.com/embed/Gt4E3rIUhoA', aa.video_url
        assert aa.video_id == 'Gt4E3rIUhoA', aa.video_id

    # games 4 and 5 not played
    def test_5_games_4_5_not_played(self):
        actual = self.parser._parse_series_page(self.get_test('cast14705-KT-Rolster-vs-Prime-Best-of-5-2014-Proleague-Round-1'))

        a = actual
        assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

        assert a.name == 'KT Rolster vs Prime (Best of 5)', a.name
        # can't get this. huh.
        assert a.path == None, a.path

        assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
        assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
        assert a.players_desc == None

        assert a.best_of == 5, a.best_of
        assert a.num_videos == 3, a.num_videos

        assert a.event.name == '2014 Proleague', a.event.name
        assert a.event_round == 'Round 1', a.event_round

        assert len(a.casters) == 1, len(a.casters)
        assert a.casters_desc == None, a.casters_desc

        assert a.cast_date == 'Jan 24, 2014', a.cast_date

        assert a.score_up == 24, a.score_up
        assert a.score_down == 2, a.score_down

        # the casts themselves
        assert len(a.casts) == a.num_videos, len(a.casts)
        # check a cast
        aa = a.casts[0]
        assert aa.__class__.__name__ == 'Sc2CastsCast', aa.__class__.__name__

        assert aa.name == 'Game 1', aa.name
        assert aa.source == 'YouTube', aa.source
        assert aa.video_url == 'https://www.youtube.com/embed/QqSRtBVEXDs', aa.video_url
        assert aa.video_id == 'QqSRtBVEXDs', aa.video_id

    def test_5_games_all_played(self):
        actual = self.parser._parse_series_page(self.get_test('cast14802-Innovation-vs-MC-Best-of-5-Warer.com-Invitational-Semi-Finals'))

        a = actual
        assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

        assert a.name == 'Innovation vs MC (Best of 5)', a.name
        # can't get this. huh.
        assert a.path == None, a.path

        assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
        assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
        assert a.players_desc == None

        assert a.best_of == 5, a.best_of
        assert a.num_videos == 5, a.num_videos

        assert a.event.name == 'Warer.com Invitational', a.event.name
        assert a.event_round == 'Semi Finals', a.event_round

        assert len(a.casters) == 1, len(a.casters)
        assert a.casters_desc == None, a.casters_desc

        assert a.cast_date == 'Feb 01, 2014', a.cast_date

        assert a.score_up == 254, a.score_up
        assert a.score_down == 9, a.score_down

        # the casts themselves
        assert len(a.casts) == a.num_videos, len(a.casts)
        # check a cast
        aa = a.casts[0]
        assert aa.__class__.__name__ == 'Sc2CastsCast', aa.__class__.__name__

        assert aa.name == 'Game 1', aa.name
        assert aa.source == 'YouTube', aa.source
        assert aa.video_url == 'https://www.youtube.com/embed/lp32OJc6zmA', aa.video_url
        assert aa.video_id == 'lp32OJc6zmA', aa.video_id

    def test_7_games_last_3_not_played(self):
        actual = self.parser._parse_series_page(self.get_test('cast14875-san-vs-Dear-Best-of-7-ASUS-ROG-Winter-2014-Finals'))

        a = actual
        assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

        assert a.name == 'san vs Dear (Best of 7)', a.name
        # can't get this. huh.
        assert a.path == None, a.path

        assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
        assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
        assert a.players_desc == None

        assert a.best_of == 7, a.best_of
        assert a.num_videos == 4, a.num_videos

        assert a.event.name == 'ASUS ROG Winter 2014', a.event.name
        assert a.event_round == 'Finals', a.event_round

        assert len(a.casters) == 1, len(a.casters)
        assert a.casters_desc == None, a.casters_desc

        assert a.cast_date == 'Feb 05, 2014', a.cast_date

        assert a.score_up == 3, a.score_up
        assert a.score_down == 1, a.score_down

        # the casts themselves
        assert len(a.casts) == a.num_videos, len(a.casts)
        # check a cast
        aa = a.casts[0]
        assert aa.__class__.__name__ == 'Sc2CastsCast', aa.__class__.__name__

        assert aa.name == 'Game 1', aa.name
        assert aa.source == 'YouTube', aa.source
        assert aa.video_url == 'https://www.youtube.com/embed/SW2jJllZUHQ', aa.video_url
        assert aa.video_id == 'SW2jJllZUHQ', aa.video_id

    def tearDown(self):
        pass

class TestIndex(unittest.TestCase):
    def setUp(self):
        with open('tests/data/index.php', 'r') as f:
            self.test_html = f.read()
        # TODO test multiple pages
        self.parser = Sc2CastsParser()

    def test_index(self):
        actual = self.parser._parse_index(self.test_html)

        expected = 19
        assert len(actual) == expected, 'Expected %i, got %i' % (expected, len(actual))

        a = actual[0]
        assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

        assert a.name == 'san vs Dear (Best of 7)', a.name
        assert a.path == '/cast14875-san-vs-Dear-Best-of-7-ASUS-ROG-Winter-2014-Finals', a.path

        assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
        assert a.matchup.name == 'PvP', a.matchup.name

        assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
        assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
        assert a.players_desc == None

        assert a.best_of == 7, a.best_of
        assert a.num_videos == 0, a.num_videos

        assert a.event.name == 'ASUS ROG Winter 2014', a.event.name
        assert a.event_round == 'Finals', a.event_round

        assert len(a.casters) == 1, len(a.casters)
        assert a.casters_desc == None, a.casters_desc

        # can't find out
        assert a.cast_date == None, a.cast_date

        # can't find out
        assert a.score_up == -1, a.score_up
        assert a.score_down == -1, a.score_down

        # the casts themselves
        # can't find out
        assert len(a.casts) == a.num_videos, len(a.casts)
        assert a.casts == [ ], a.casts

    def tearDown(self):
        pass

class TestAll(unittest.TestCase):
    def setUp(self):
        with open('tests/data/all', 'r') as f:
            self.test_html = f.read()
        # TODO test multiple pages
        self.parser = Sc2CastsParser()

    def test_all(self):
        actual = self.parser._parse_all(self.test_html)

        expected = 100
        assert len(actual) == expected, 'Expected %i, got %i' % (expected, len(actual))

        a = actual[0]
        assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

        assert a.name == 'san vs Dear (Best of 7)', a.name
        assert a.path == '/cast14875-san-vs-Dear-Best-of-7-ASUS-ROG-Winter-2014-Finals', a.path

        assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
        assert a.matchup.name == 'PvP', a.matchup.name

        assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
        assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
        assert a.players_desc == None

        assert a.best_of == 7, a.best_of
        assert a.num_videos == 0, a.num_videos

        assert a.event.name == 'ASUS ROG Winter 2014', a.event.name
        assert a.event_round == 'Finals', a.event_round

        assert len(a.casters) == 1, len(a.casters)
        assert a.casters_desc == None, a.casters_desc

        # can't find out
        assert a.cast_date == None, a.cast_date

        # can't find out
        assert a.score_up == -1, a.score_up
        assert a.score_down == -1, a.score_down

        # the casts themselves
        # can't find out
        assert len(a.casts) == a.num_videos, len(a.casts)
        assert a.casts == [ ], a.casts

    def tearDown(self):
        pass

class TestTop(unittest.TestCase):
    def setUp(self):
        self.parser = Sc2CastsParser()

    def test_top(self):
        with open('tests/data/top', 'r') as f:
            self.test_html = f.read()
        actual = self.parser._parse_top(self.test_html)

        expected = 20
        assert len(actual) == expected, 'Expected %i, got %i' % (expected, len(actual))

        # check some in detail

        a = actual[0]
        assert a.__class__.__name__ == 'Sc2CastsSeries'

        assert a.name == 'CatZ vs TheStC (Best of 5)', a.name
        assert a.path == '/cast14824-CatZ-vs-TheStC-Best-of-5-2014-WCS-America-Challenger-League', a.path

        assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
        assert a.matchup.name == 'ZvT', a.matchup.name

        assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
        assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
        assert a.players_desc == None

        assert a.best_of == 5, a.best_of
        # can't find out
        assert a.num_videos == 0, a.num_videos

        assert a.event.name == '2014 WCS America', a.event.name
        assert a.event_round == 'Challenger League', a.event_round

        assert len(a.casters) == 1, len(a.casters)
        assert a.casters[0].__class__.__name__ == 'Sc2CastsCaster'
        assert a.casters_desc == None, a.casters_desc

        # can't find out
        assert a.cast_date == None, a.cast_date

        assert a.score_up == -1, a.score_up
        assert a.score_down == -1, a.score_down

        # the casts themselves
        # can't find out
        assert len(a.casts) == a.num_videos, len(a.casts)
        assert a.casts == [ ], a.casts

    def test_top_month(self):
        with open('tests/data/top?month', 'r') as f:
            self.test_html = f.read()
        actual = self.parser._parse_top(self.test_html)

        expected = 20
        assert len(actual) == expected, 'Expected %i, got %i' % (expected, len(actual))

        # check some in detail

        a = actual[0]
        assert a.__class__.__name__ == 'Sc2CastsSeries'

        assert a.name == 'Innovation vs MC (Best of 5)', a.name
        assert a.path == '/cast14802-Innovation-vs-MC-Best-of-5-Warer.com-Invitational-Semi-Finals', a.path

        assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
        assert a.matchup.name == 'TvP', a.matchup.name

        assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
        assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
        assert a.players_desc == None

        assert a.best_of == 5, a.best_of
        # can't find out
        assert a.num_videos == 0, a.num_videos

        assert a.event.name == 'Warer.com Invitational', a.event.name
        assert a.event_round == 'Semi Finals', a.event_round

        assert len(a.casters) == 1, len(a.casters)
        assert a.casters[0].__class__.__name__ == 'Sc2CastsCaster'
        assert a.casters_desc == None, a.casters_desc

        # can't find out
        assert a.cast_date == None, a.cast_date

        assert a.score_up == -1, a.score_up
        assert a.score_down == -1, a.score_down

        # the casts themselves
        # can't find out
        assert len(a.casts) == a.num_videos, len(a.casts)
        assert a.casts == [ ], a.casts


    def tearDown(self):
        pass

class TestBrowse(unittest.TestCase):
    def setUp(self):
        with open('tests/data/browse', 'r') as f:
            self.test_html = f.read()
        self.parser = Sc2CastsParser()

    def test_casters(self):
        actual = self.parser.casters(self.test_html)

        expected = 636
        assert len(actual) == expected, 'Expected %i, got %i' % (expected, len(actual))

    def test_events(self):
        actual = self.parser.events(self.test_html)

        expected = 554
        assert len(actual) == expected, 'Expected %i, got %i' % (expected, len(actual))

    def test_matchups(self):
        actual = self.parser.matchups(self.test_html)

        expected = 6
        assert len(actual) == expected, 'Expected %i, got %i' % (expected, len(actual))

    def test_players(self):
        actual = self.parser.players(self.test_html)

        expected = 182
        assert len(actual) == expected, 'Expected %i, got %i' % (expected, len(actual))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
