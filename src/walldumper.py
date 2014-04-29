#!/usr/bin/env python
import urllib.request, re, sys, dumperutils

def parse(url):
    r = re.search("([^/]+?)(.png|.jpg|.jpeg)$", url)
    if r:
        #OMG A DIRECT LINK
        dumperutils.store(r.group(1) + r.group(2), url)
        return

    r = re.search("^https?://i.imgur.com/([^/]+?)(.png|.jpg|.jpeg).+?", url)
    if r:
        #stupid fix for urls like http://i.imgur.com/EZ20NyV.jpg?1
        dumperutils.store(r.group(1) + r.group(2), url)
        return

    r = re.search("^https?://imgur.com/a/[^/]+?", url)
    if r:
        #HURR DURR A IMGUR ALBUM
        dumperutils.imguralbum(url)
        return

    r = re.search("^https?://imgur.com/[^/.]+?$", url)
    if r:
        #Y U NO POST DIRECT LINK
        dumperutils.imgursingle(url)
        return

    r = re.search("cloud-\d\.steampowered\.com/.+?", url)
    if r:
        #who the fuck uses steam screenshots as wallpapers? me!
        dumperutils.steamscreen(url)
        return

    print("nope (" + url + ")")

#url = "https://www.reddit.com/r/wallpapers/top/?sort=top&t=day"
url = sys.argv[1]
html = urllib.request.urlopen(url).read().decode("UTF-8")
for s in re.findall("<a.+?class=\".+?thumbnail.+?\".+?href=\"(.+?)\".+?>.+?</a>", html):
    parse(s)
