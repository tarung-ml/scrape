# Given an app, this function collects the linkedin URLs of founders

# Main steps in the process:
# Step 1: Perform a google search for " $AppName + founder + linkedin"
# Step 2: Collect URLS of top 4 search results
# Step 3: Filter out non-linkedin URLs
# Step 4: Return the set of linkedin profile URLs

import json
import urllib
import urllib.parse 
import urllib.request
import time
def returnFounders(app):
  result = []
  searchfor = app + " app founder linkedin"
  query = urllib.parse.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.request.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results.decode())
  data = results['responseData']
  hits = data['results']
  print ('Top %d hits:' % len(hits))
  for h in hits: 
    print (' ', h['url'])
    if (h not in result):
        result.append(h['url'])
  print ('For more results, see %s' % data['cursor']['moreResultsUrl'])
  time.sleep(1)
#add more search results
  searchfor = app + " founder linkedin"
  query = urllib.parse.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.request.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results.decode())
  data = results['responseData']
  hits = data['results']
  print ('Top %d hits:' % len(hits))
  for h in hits: 
    print (' ', h['url'])
    result.append(h['url'])
    if (h not in result):
        result.append(h['url'])
  print ('For more results, see %s' % data['cursor']['moreResultsUrl'])
  urls_filtered = [x for x in result if ("linkedin.com/in/" in x) or ("linkedin.com/pub/" in x) ]
  return (set(urls_filtered))

