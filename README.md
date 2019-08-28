# MGMwerx-scraper

MGMwerx-scraper is a docker container project that runs in RedHat OpenShift <BR/>
<BR/>
The following websites are scraped using <a href="https://scrapy.org/">Scrapy</a> and <a href="https://scrapyd.readthedocs.io/en/stable/">Scrapyd</a> for calendar event data:<BR/>
<UL>
<LI>Eventbrite - https://www.eventbrite.com/d/al--montgomery/events/</LI>
<LI>Gumptown Magazine - https://gumptownmag.com/events/</LI>
<LI>Know the Community -http://knowthecommunity.com/explore-calendar/</LI>
<LI>Life At The Max - https://www.lifeatthemax.us/calendar</LI>
<LI>Montgomery Chamber - https://www.montgomerychamber.com/events</LI>
<LI>Montgomery Parents Magazine - http://montgomeryparents.com/index.php/family-calendar/</LI>
<LI>River Region's Journey - http://readjourneymagazine.com/index.php?option=com_k2&view=item&layout=item&id=222&Itemid=119</LI>
<LI>RSVP Montgomery - http://www.rsvp-montgomery.com/events</LI>
<LI>Visiting Montgomery - https://visitingmontgomery.com/calendar/</LI>
</UL>
<BR/>
Command line to launch container on OpenShift:<BR/>
oc login https://afitc.redhatgov.io/<BR/>
oc new-app https://github.com/mgmwerx/scraper --name zach --strategy=docker<BR/>
<BR/>
TODO:<BR/>
<UL>
<LI>QA each spider to ensure each is extracting all required data</LI>
<LI>Standardize start and end date format in each spider</LI>
<LI>Standardize category data format accross scrapers.  Should be JSON array, but currently some scrapers have comma delimited list</LI>
<LI>Some spiders require a 'details' page to be clicked and additional data to be extracted</LI>
<LI>Scrape additional websites:<BR/>
ALMETRO 360 - need website url<BR/>
Montgomery Independent - https://www.montgomeryindependent.com/calendar/<BR/>
Montgomery Advertiser - http://events.montgomeryadvertiser.com/<BR/>
River Region Boom - http://riverregionboom.com/<BR/>
Bulletin Board Classifieds - need website url<BR/>
TidBits Weekly - http://www.tidbitsweekly.com/news-events<BR/>
TriCounty Homes - https://www.tri-countyads.com/<BR/>
</LI>
<LI>Use NLP to extract data from unstructured text on certain websites.  See POC in project's /nlp folder</LI>
</UL>
