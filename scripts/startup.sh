#!/bin/bash

# turn on bash's job control
set -m

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
curl http://127.0.0.1/addversion.json -F project=scraper -F version=r23 -F egg=@dist/scraper-1.0-py3.7.egg
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to upload egg: $status"
  exit $status
fi

#list spiders
curl http://127.0.0.1/listspiders.json?project=scraper

# call each scraper
curl http://127.0.0.1/schedule.json -d project=scraper -d spider=mgmchamber-spider
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to call MGM Chamber scraper: $status"
  exit $status
fi

# now we bring the primary process back into the foreground
# and leave it there
fg %1
