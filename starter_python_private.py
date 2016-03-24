# Scrapes profile from saved html of private profile
# Example: result = returnPrivateProfile('/Users/tarun/demo.html')

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
def returnPrivateProfile(path):
    req = Request("file:///" + path, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html)
    profile = {}
    profile['name'] = soup.find('span','full-name').string
    return profile
