from bs4 import BeautifulSoup
import urllib2

url = "https://www.montgomerychamber.com/events"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, features="lxml")

print soup

print soup.title.string
