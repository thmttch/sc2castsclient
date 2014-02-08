#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sc2castsclient import *

if __name__ == '__main__':
    client = Sc2CastsClient()

    print('Current series on sc2casts.com main page:')

    for series in client.series():
        print(series.name)
