#!/usr/bin/env bash

links=(
http://sc2casts.com/index.php
http://sc2casts.com/all
http://sc2casts.com/all:page=2
http://sc2casts.com/browse
http://sc2casts.com/top
http://sc2casts.com/top?p=2
http://sc2casts.com/top?month
'http://sc2casts.com/top?month=&p=2'
http://sc2casts.com/top?week
'http://sc2casts.com/top?week=&p=2'
http://sc2casts.com/cast14719-Soulkey-vs-Cure-Best-of-3-All-in-1-video-IEM-Cologne-2014-Korean-Qualifier
http://sc2casts.com/cast14705-KT-Rolster-vs-Prime-Best-of-5-2014-Proleague-Round-1
http://sc2casts.com/cast14802-Innovation-vs-MC-Best-of-5-Warer.com-Invitational-Semi-Finals
http://sc2casts.com/cast14875-san-vs-Dear-Best-of-7-ASUS-ROG-Winter-2014-Finals
)

for link in "${links[@]}"; do
  # -N for overwrite
  wget -N "$link"
done
