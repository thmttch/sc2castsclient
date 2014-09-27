#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from parser import Sc2CastsParser

# deals only with network requests; parsing is done elsewhere
class Sc2CastsClient:

    HOST = 'http://sc2casts.com'

    PATH_INDEX = '/index.php'
    PATH_TOP_24H = '/top'
    PATH_TOP_WEEK = '/top?week'
    PATH_TOP_MONTH = '/top?month'
    PATH_TOP_ALL = '/top?all'
    #PATH_BROWSE = '/browse'
    PATH_ALL = '/all'

    USER_AGENT = ''

    def log(self, message):
        print message

    def __init__(self, user_agent=USER_AGENT):
        self.parser = Sc2CastsParser()
        self.user_agent = user_agent

    def series(self, filtertype='recent'):
        '''
        Query/filter for getting one or more casts, by 'type':

        { recent, top_24h, top_week, top_month, top_all, best_of_201[0123], all }
        '''
        if filtertype not in [ 'recent', 'top_24h', 'top_week', 'top_month', 'top_all', 'all' ]:
            self.log('Unknown filtertype: ' + filtertype + '. Assuming recent')
            filtertype = 'recent'

        if filtertype == 'recent':
            url = self.HOST + self.PATH_INDEX
            html = requests.get(url).text
            return self.parser._parse_index(html)
        elif filtertype == 'top_24h':
            url = self.HOST + self.PATH_TOP_24H
            html = requests.get(url).text
            return self.parser._parse_top(html)
        elif filtertype == 'top_week':
            url = self.HOST + self.PATH_TOP_WEEK
            html = requests.get(url).text
            return self.parser._parse_top(html)
        elif filtertype == 'top_month':
            url = self.HOST + self.PATH_TOP_MONTH
            html = requests.get(url).text
            return self.parser._parse_top(html)
        elif filtertype == 'top_all':
            url = self.HOST + self.PATH_TOP_ALL
            html = requests.get(url).text
            return self.parser._parse_top(html)
        elif filtertype == 'all':
            url = self.HOST + self.PATH_ALL
            html = requests.get(url).text
            return self.parser._parse_all(html)

    def series_by_path(self, path):
        url = self.HOST + path
        html = requests.get(url).text
        return self.parser._parse_series_page(html)
