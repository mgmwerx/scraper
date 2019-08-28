#!/bin/bash

export PODNAME=$(echo "$HOSTNAME" | cut -d- -f1)
export URL="$PODNAME-scraper.apps.afitc.redhatgov.io"

# turn on bash's job control
set -m

# Start scrapyd
python ./app.py &

# create egg
python ./setup.py bdist_egg

# upload egg
curl http://$URL/addversion.json -F project=scraper -F version=r23 -F egg=@dist/scraper-1.0-py3.7.egg

#list spiders
curl http:///$URL/listspiders.json?project=scraper

# call each scraper
curl http:///$URL/schedule.json -d project=scraper -d spider=eventbrite-spider

curl http:///$URL/schedule.json -d project=scraper -d spider=gumptonwn-spider

curl http:///$URL/schedule.json -d project=scraper -d spider=knowTheCommunity-spider

curl http:///$URL/schedule.json -d project=scraper -d spider=lifeatthemax-spider

curl http:///$URL/schedule.json -d project=scraper -d spider=mgmchamber-spider

curl http:///$URL/schedule.json -d project=scraper -d spider=mgmparents-spider

curl http:///$URL/schedule.json -d project=scraper -d spider=riverregion-spider

curl http:///$URL/schedule.json -d project=scraper -d spider=rsvpMontgomery-spider

curl http:///$URL/schedule.json -d project=scraper -d spider=visitingMontgomery-spider

# now we bring the primary process back into the foreground
# and leave it there
fg %1
