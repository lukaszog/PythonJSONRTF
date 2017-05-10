# info ze strony http://python-history.blogspot.com/feeds/posts/default?alt=json
import urllib2
import json

url = "http://python-history.blogspot.com/feeds/posts/default?alt=json"
site = urllib2.urlopen(url)

data = json.load(site)

for dump in data['feed']['entry']:
    print dump['title']['$t']   #wszystkie tytuly
    print dump['published']['$t'] #wszystkie daty
    print dump['content']['$t'] #wszystkie tresci


