from bs4 import BeautifulSoup
import urllib2

url = "https://www.montgomerychamber.com/events"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, features="lxml")

#print soup


print soup.title.string
for link in soup.find_all('div', class_='mn-title'):
        print link
        #print link.get('href')
     
