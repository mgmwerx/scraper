#!/bin/bash

# turn on bash's job control
set -m

export PODNAME=$(echo "$HOSTNAME" | cut -d- -f1)
export URL="$PODNAME-scraper.apps.afitc.redhatgov.io"
echo $URL

# Start scrapyd
python ./app.py &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start scrapyd: $status"
  exit $status
fi

# create egg
python ./setup.py bdist_egg
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to build egg: $status"
  exit $status
fi

# upload egg
curl http://$URL/addversion.json -F project=scraper -F version=r23 -F egg=@dist/scraper-1.0-py3.7.egg
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to upload egg: $status"
  exit $status
fi

#wait 5 seconds for egg to deploy
sleep 5s

#list spiders
curl http:///$URL/listspiders.json?project=scraper


# call each scraper
curl http:///$URL/schedule.json -d project=scraper -d spider=mgmchamber-spider
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to call MGM Chamber scraper: $status"
  exit $status
fi

# now we bring the primary process back into the foreground
# and leave it there
fg %1
