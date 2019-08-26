from bs4 import BeautifulSoup
import requests

url = "https://www.montgomerychamber.com/events"

#content = urllib2.urlopen(url).read()
req = requests.get(url)
#print (req.content)
soup = BeautifulSoup(req.content)

#print soup


print (soup.title.string)
for link in soup.find_all('div', class_='mn-title'):
        print (link)
        #print link.get('href')
     
