# Scrapes public profile given a public profile url
# Example: result = returnPublicProfile('https://www.linkedin.com/in/anandrajaraman')

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
def returnPublicProfile(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html)
    profile = {}
    profile['name'] = soup.find('h1','fn').string
    profile['location'] = soup.find('span','locality').string
    profile['title'] = soup.find('p','headline title').string
    profile['skills'] = [skill.string for skill in soup.find('ul','pills').findAll('span', 'wrap')]
    #soup.find("ul","schools").find("h4", "item-title").string
    return profile
