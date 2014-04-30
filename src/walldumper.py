#!/usr/bin/env python
import urllib.request, re, argparse, dumperutils

def redditparse(url):
    rxs = {"([^/]+?)(.png|.jpg|.jpeg)$": dumperutils.store,
        "^https?://i.imgur.com/([^/]+?)(.png|.jpg|.jpeg).+?": dumperutils.store,
        "^https?://imgur.com/a/[^/]+?": dumperutils.imguralbum,
        "^https?://imgur.com/[^/.]+?$": dumperutils.imgursingle,
        "cloud-\d\.steampowered\.com/.+?": dumperutils.steamscreen}

    for rx in rxs:
        if re.search(rx, url): rxs[rx](url)

def chanthread(board, message):
    if not(message in ["4667225", "4667232"]):
        url = "https://boards.4chan.org/" + board + "/thread/" + message
        dumperutils.chandump(url, board)

parser = argparse.ArgumentParser(description='walldumper.py, a wallpaper dumper for wallfags.')
parser.add_argument('-t','--type', help='Website type ("reddit" or "4chan")', required=True)
parser.add_argument('-b','--board', help='Board name ("wallpapers" for reddit, "wg" for 4chan)', required=True)
args = vars(parser.parse_args())

if args["type"] == "reddit":
    html = urllib.request.urlopen("https://reddit.com/r/" + args["board"]).read().decode("UTF-8")
    for s in re.findall("<a.+?class=\".+?thumbnail.+?\".+?href=\"(.+?)\".+?>.+?</a>", html):
        redditparse(s)

elif args["type"] == "4chan":
    html = urllib.request.urlopen("https://boards.4chan.org/" + args["board"]).read().decode("UTF-8")
    for s in re.findall("<blockquote.+?class=\"postMessage\".+?id=\"m(\d+)\">.+?</blockquote>", html):
        chanthread(args["board"], s)

else:
    print("The TYPE argument must be either reddit or 4chan for this to work")
