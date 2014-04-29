#!/usr/bin/env python
import urllib.request, re, sys, dumperutils

def parse(url):
    rxs = {"([^/]+?)(.png|.jpg|.jpeg)$": dumperutils.store,
        "^https?://i.imgur.com/([^/]+?)(.png|.jpg|.jpeg).+?": dumperutils.store,
        "^https?://imgur.com/a/[^/]+?": dumperutils.imguralbum,
        "^https?://imgur.com/[^/.]+?$": dumperutils.imgursingle,
        "cloud-\d\.steampowered\.com/.+?": dumperutils.steamscreen}

    for rx in rxs:
        if re.search(rx, url): rxs[rx](url)

url = sys.argv[1]
html = urllib.request.urlopen(url).read().decode("UTF-8")
for s in re.findall("<a.+?class=\".+?thumbnail.+?\".+?href=\"(.+?)\".+?>.+?</a>", html):
    parse(s)
