#!/usr/bin/env python

def assert_cast14719(actual):
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

    assert a.name == 'Soulkey vs Cure (BO3 in 1 video)', a.name
    # can't get this. huh.
    assert a.path == None, a.path

    assert a.source == 'YouTube', a.source

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

    assert a.source == 'YouTube', a.source

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

    assert a.source == 'YouTube', a.source

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

    assert a.source == 'YouTube', a.source

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
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

    assert a.name == 'WelMu vs Ryung (Best of 3)', a.name
    assert a.path == '/cast16700-WelMu-vs-Ryung-Best-of-3-DreamHack-Stockholm-2014-Group-Stage-3', a.path

    assert a.source == 'YouTube', a.source

    assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
    # team game: currently uses empty matchup tag
    assert a.matchup.name == 'PvT', a.matchup.name

    assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
    assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
    assert a.players_desc == None

    assert a.best_of == 3, a.best_of
    assert a.num_videos == 0, a.num_videos

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

def assert_cast17091(actual):
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

    assert a.name == 'TLO vs LosirA (BO3 in 1 Video)', a.name
    assert a.path == '/cast17091-TLO-vs-LosirA-Best-of-3-All-in-1-video-HomeStory-Cup-X-Group-Stage-2', a.path

    assert a.source == 'Twitch', a.source

    assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
    # team game: currently uses empty matchup tag
    assert a.matchup.name == 'ZvZ', a.matchup.name

    assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
    assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
    assert a.players_desc == None

    assert a.best_of == 3, a.best_of
    assert a.num_videos == 0, a.num_videos

    assert a.event.name == 'HomeStory Cup X', a.event.name
    assert a.event_round == 'Group Stage 2', a.event_round

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
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

    assert a.name == 'Grubby vs Ryung (Best of 3)', a.name
    assert a.path == '/cast16698-Grubby-vs-Ryung-Best-of-3-DreamHack-Stockholm-2014-Group-Stage-3', a.path

    assert a.source == 'YouTube', a.source

    assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
    assert a.matchup.name == 'PvT', a.matchup.name

    assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
    assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
    assert a.players_desc == None

    assert a.best_of == 3, a.best_of
    assert a.num_videos == 0, a.num_videos

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

def assert_cast17089(actual):
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries', a.__class__.__name__

    assert a.name == 'Flash vs LosirA (BO3 in 1 Video)', a.name
    assert a.path == '/cast17089-Flash-vs-LosirA-Best-of-3-All-in-1-video-HomeStory-Cup-X-Group-Stage-2', a.path

    assert a.source == 'Twitch', a.source

    assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
    assert a.matchup.name == 'TvZ', a.matchup.name

    assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
    assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
    assert a.players_desc == None

    assert a.best_of == 3, a.best_of
    assert a.num_videos == 0, a.num_videos

    assert a.event.name == 'HomeStory Cup X', a.event.name
    assert a.event_round == 'Group Stage 2', a.event_round

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

    assert a.name == 'MC vs Dayshi (BO3 in 1 Video)', a.name
    assert a.path == '/cast16691-MC-vs-Dayshi-Best-of-3-All-in-1-video-2014-WCS-Europe-S3-Group-Stage-2', a.path

    assert a.source == 'YouTube', a.source

    assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
    assert a.matchup.name == 'PvT', a.matchup.name

    assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
    assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
    assert a.players_desc == None

    assert a.best_of == 3, a.best_of
    # can't find out
    assert a.num_videos == 0, a.num_videos

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

def assert_cast16892(actual):
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries'

    assert a.name == 'Bbyong vs Soulkey (Best of 3)', a.name
    assert a.path == '/cast16892-Bbyong-vs-Soulkey-Best-of-3-2014-GSL-Season-3-Code-S-Round-of-32', a.path

    assert a.source == 'YouTube', a.source

    assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
    assert a.matchup.name == 'TvZ', a.matchup.name

    assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
    assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
    assert a.players_desc == None

    assert a.best_of == 3, a.best_of
    # can't find out
    assert a.num_videos == 0, a.num_videos

    assert a.event.name == '2014 GSL Season 3 Code S', a.event.name
    assert a.event_round == 'Round of 32', a.event_round

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

    assert a.source == 'YouTube', a.source

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

def assert_cast17011(actual):
    a = actual
    assert a.__class__.__name__ == 'Sc2CastsSeries'

    assert a.name == 'Zest vs Life (Best of 5)', a.name
    assert a.path == '/cast17011-Zest-vs-Life-Best-of-5-2014-WCS-Global-Finals-Round-of-16', a.path

    assert a.source == 'YouTube', a.source

    assert a.matchup.__class__.__name__ == 'Sc2CastsMatchup'
    assert a.matchup.name == 'PvZ', a.matchup.name

    assert len(a.players) == 2, str(len(a.players)) + ": " + str(a.players)
    assert a.players[0].__class__.__name__ == 'Sc2CastsPlayer', a.players[0]
    assert a.players_desc == None

    assert a.best_of == 5, a.best_of
    # can't find out
    assert a.num_videos == 0, a.num_videos

    assert a.event.name == '2014 WCS Global Finals', a.event.name
    assert a.event_round == 'Round of 16', a.event_round

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
