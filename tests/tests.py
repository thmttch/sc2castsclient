#!/usr/bin/env python

def assert_cast14719(actual):
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

    assert a.name == 'Soulkey vs Cure (BO3 in 1 video)', a.name
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

    assert a.cast_date is None, a.cast_date
    assert a.post_date == 'Jan 24, 2014', a.post_date

    assert a.score_up == 29, a.score_up
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

def assert_cast14705(actual):
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

    assert a.cast_date is None, a.cast_date
    assert a.post_date == 'Jan 24, 2014', a.post_date

    assert a.score_up == 27, a.score_up
    assert a.score_down == 3, a.score_down

    # the casts themselves
    assert len(a.casts) == a.num_videos, len(a.casts)
    # check a cast
    aa = a.casts[0]
    assert aa.__class__.__name__ == 'Sc2CastsCast', aa.__class__.__name__

    assert aa.name == 'Game 1', aa.name
    assert aa.source == 'YouTube', aa.source
    assert aa.video_url == 'https://www.youtube.com/embed/QqSRtBVEXDs', aa.video_url
    assert aa.video_id == 'QqSRtBVEXDs', aa.video_id

def assert_cast14802(actual):
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

    assert a.cast_date is None, a.cast_date
    assert a.post_date == 'Feb 01, 2014', a.post_date

    assert a.score_up == 327, a.score_up
    assert a.score_down == 11, a.score_down

    # the casts themselves
    assert len(a.casts) == a.num_videos, len(a.casts)
    # check a cast
    aa = a.casts[0]
    assert aa.__class__.__name__ == 'Sc2CastsCast', aa.__class__.__name__

    assert aa.name == 'Game 1', aa.name
    assert aa.source == 'YouTube', aa.source
    assert aa.video_url == 'https://www.youtube.com/embed/lp32OJc6zmA', aa.video_url
    assert aa.video_id == 'lp32OJc6zmA', aa.video_id

def assert_cast14875(actual):
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

    assert a.cast_date is None, a.cast_date
    assert a.post_date == 'Feb 05, 2014', a.post_date

    assert a.score_up == 28, a.score_up
    assert a.score_down == 7, a.score_down

    # the casts themselves
    assert len(a.casts) == a.num_videos, len(a.casts)
    # check a cast
    aa = a.casts[0]
    assert aa.__class__.__name__ == 'Sc2CastsCast', aa.__class__.__name__

    assert aa.name == 'Game 1', aa.name
    assert aa.source == 'YouTube', aa.source
    assert aa.video_url == 'https://www.youtube.com/embed/SW2jJllZUHQ', aa.video_url
    assert aa.video_id == 'SW2jJllZUHQ', aa.video_id

def assert_cast16700(actual):
    #a = actual[0]
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

    #assert a.name == 'MaNa vs MMA (BO3 in 1 Video)', a.name
    assert a.name == 'WelMu vs Ryung (Best of 3)', a.name
    #assert a.path == '/cast16687-MaNa-vs-MMA-Best-of-3-All-in-1-video-2014-WCS-Europe-S3-Group-Stage-2', a.path
    assert a.path == '/cast16700-WelMu-vs-Ryung-Best-of-3-DreamHack-Stockholm-2014-Group-Stage-3', a.path

    assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
    # team game: currently uses empty matchup tag
    assert a.matchup.name == 'PvT', a.matchup.name

    assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
    assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
    assert a.players_desc == None

    assert a.best_of == 3, a.best_of
    assert a.num_videos == 0, a.num_videos

    #assert a.event.name == '2014 WCS Europe S3', a.event.name
    assert a.event.name == 'DreamHack Stockholm 2014', a.event.name
    #assert a.event_round == 'Group Stage 2', a.event_round
    assert a.event_round == 'Group Stage 3', a.event_round

    assert len(a.casters) == 1, len(a.casters)
    assert a.casters_desc == None, a.casters_desc

    # can't find out
    assert a.cast_date == None, a.cast_date
    assert a.post_date == None, a.post_date

    # can't find out
    assert a.score_up == -1, a.score_up
    assert a.score_down == -1, a.score_down

    # the casts themselves
    # can't find out
    assert len(a.casts) == a.num_videos, len(a.casts)
    assert a.casts == [ ], a.casts

def assert_cast16698(actual):
    #a = actual[2]
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

    #assert a.name == 'WelMu vs MaNa (BO3 in 1 Video)', a.name
    assert a.name == 'Grubby vs Ryung (Best of 3)', a.name
    #assert a.path == '/cast16685-WelMu-vs-MaNa-Best-of-3-All-in-1-video-2014-WCS-Europe-S3-Group-Stage-2', a.path
    assert a.path == '/cast16698-Grubby-vs-Ryung-Best-of-3-DreamHack-Stockholm-2014-Group-Stage-3', a.path

    assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
    #assert a.matchup.name == 'PvP', a.matchup.name
    assert a.matchup.name == 'PvT', a.matchup.name

    assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
    assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
    assert a.players_desc == None

    assert a.best_of == 3, a.best_of
    assert a.num_videos == 0, a.num_videos

    #assert a.event.name == '2014 WCS Europe S3', a.event.name
    assert a.event.name == 'DreamHack Stockholm 2014', a.event.name
    assert a.event_round == 'Group Stage 3', a.event_round

    assert len(a.casters) == 1, len(a.casters)
    assert a.casters_desc == None, a.casters_desc

    # can't find out
    assert a.cast_date == None, a.cast_date
    assert a.post_date == None, a.post_date

    # can't find out
    assert a.score_up == -1, a.score_up
    assert a.score_down == -1, a.score_down

    # the casts themselves
    # can't find out
    assert len(a.casts) == a.num_videos, len(a.casts)
    assert a.casts == [ ], a.casts

def assert_cast16691(actual):
    #a = actual[0]
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries'

    #assert a.name == 'Pigbaby vs TaeJa (BO3 in 1 Video)', a.name
    assert a.name == 'MC vs Dayshi (BO3 in 1 Video)', a.name
    #assert a.path == '/cast16658-Pigbaby-vs-TaeJa-Best-of-3-All-in-1-video-2014-WCS-America-S3-Group-Stage-2', a.path
    assert a.path == '/cast16691-MC-vs-Dayshi-Best-of-3-All-in-1-video-2014-WCS-Europe-S3-Group-Stage-2', a.path

    assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
    assert a.matchup.name == 'PvT', a.matchup.name

    assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
    assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
    assert a.players_desc == None

    assert a.best_of == 3, a.best_of
    # can't find out
    assert a.num_videos == 0, a.num_videos

    #assert a.event.name == '2014 WCS America S3', a.event.name
    assert a.event.name == '2014 WCS Europe S3', a.event.name
    assert a.event_round == 'Group Stage 2', a.event_round

    assert len(a.casters) == 1, len(a.casters)
    assert a.casters[0].__class__.__name__ == 'Sc2CastsCaster'
    assert a.casters_desc == None, a.casters_desc

    # can't find out
    assert a.cast_date == None, a.cast_date
    assert a.post_date == None, a.post_date

    assert a.score_up == -1, a.score_up
    assert a.score_down == -1, a.score_down

    # the casts themselves
    # can't find out
    assert len(a.casts) == a.num_videos, len(a.casts)
    assert a.casts == [ ], a.casts

def assert_cast16666(actual):
    #a = actual[0]
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries'

    assert a.name == 'Scarlett vs PartinG (Best of 3)', a.name
    assert a.path == '/cast16666-Scarlett-vs-PartinG-Best-of-3-Red-Bull-Battle-Grounds:-Washington-Group-Stage', a.path

    assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
    assert a.matchup.name == 'ZvP', a.matchup.name

    assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
    assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
    assert a.players_desc == None

    assert a.best_of == 3, a.best_of
    # can't find out
    assert a.num_videos == 0, a.num_videos

    assert a.event.name == 'Red Bull Battle Grounds: Washington', a.event.name
    assert a.event_round == 'Group Stage', a.event_round

    assert len(a.casters) == 1, len(a.casters)
    assert a.casters[0].__class__.__name__ == 'Sc2CastsCaster'
    assert a.casters_desc == None, a.casters_desc

    # can't find out
    assert a.cast_date == None, a.cast_date
    assert a.post_date == None, a.post_date

    assert a.score_up == -1, a.score_up
    assert a.score_down == -1, a.score_down

    # the casts themselves
    # can't find out
    assert len(a.casts) == a.num_videos, len(a.casts)
    assert a.casts == [ ], a.casts


'''
#from sc2casts_parser import *
from sc2casts_client import *
import json
from pprint import *

parser = SC2CastsParser()
client = SC2CastsClient()
TEST_DATA_DIR = 'data'

# test cases:

def test_titles():
    pass

# test cases:

def test_casts():
    with open(TEST_DATA_DIR + '/all', 'r') as f:
        test_data = f.read()
        #print test_data

    actual = parser.casts(test_data)
    pprint(actual)

    # TODO check each cast

# test cases:
# bo3 in 1 game
# 1 game
# 3 games
# 5 games

def test_games_bo3_in_1_game():
    with open(TEST_DATA_DIR + '/cast14719-Soulkey-vs-Cure-Best-of-3-All-in-1-video-IEM-Cologne-2014-Korean-Qualifier', 'r') as f:
        test_data = f.read()
        #print test_data

    actual = parser.games(test_data)

    assert len(actual) == 1

    assert actual[0]['game_id'] == 'Gt4E3rIUhoA'
    assert actual[0]['game_title'] == 'Game 1'

# games 4 and 5 not played
def test_games_5_games():
    with open(TEST_DATA_DIR + '/cast14705-KT-Rolster-vs-Prime-Best-of-5-2014-Proleague-Round-1', 'r') as f:
        test_data = f.read()
        #print test_data

    actual = parser.games(test_data)

    print actual
    assert len(actual) == 5

    assert actual[0]['game_id'] == 'QqSRtBVEXDs'
    assert actual[0]['game_title'] == 'Game 1'

    assert actual[1]['game_id'] == '5lFLuOKYTa8'
    assert actual[1]['game_title'] == 'Game 2'

    assert actual[2]['game_id'] == 'wNhcT-NenNs'
    assert actual[2]['game_title'] == 'Game 3'

    assert actual[3]['game_id'] == ''
    assert actual[3]['game_title'] == 'Game 4'

    assert actual[4]['game_id'] == ''
    assert actual[4]['game_title'] == 'Game 5'

# test cases:

def test_events():
    with open(TEST_DATA_DIR + '/browse', 'r') as f:
        test_data = f.read()

    actual = parser.events(test_data)
    pprint(actual)

# test cases:

def test_casters():
    with open(TEST_DATA_DIR + '/browse', 'r') as f:
        test_data = f.read()

    actual = parser.casters(test_data)
    pprint(actual)

# test cases:

def test_matchups():
    with open(TEST_DATA_DIR + '/browse', 'r') as f:
        test_data = f.read()

    actual = parser.matchups(test_data)

    assert len(actual) == 6
    # TODO test that the actual URLs are still valid

# client tests

def test_client_matchups():
    actual = client.matchups()
    assert len(actual) == 6

'''
