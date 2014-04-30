import urllib.request, urllib.error, re

def store(url, name = ""):
    if name == "":
        r = re.search("([^/]+?)(.png|.jpg|.jpeg)$", url)
        if r:
            store(url, r.group(1) + r.group(2))
    else:
        print("[~] Downloading " + url + " -> " + name)
        f = urllib.request.urlopen(url)
        with open(name, "b+w") as g:
            g.write(f.read())

def imguralbum(url):
    html = urllib.request.urlopen(url).read().decode("UTF-8")
    for s in re.findall("<a.+?class=\"zoom\".+?href=\"(.+?)\">", html):
        r = re.search("([^/]+?)(.png|.jpg|.jpeg)$", s)
        store("https:" + s, r.group(1) + r.group(2))

def imgursingle(url):
    html = urllib.request.urlopen(url).read().decode("UTF-8")
    r = re.search("<a.+?href=\".+?/([^/]+?)(.png|.jpg|.jpeg)\">", html)
    if r:
        store(url, r.group(1) + r.group(2))

def steamscreen(url):
    r = re.search(".+?/([^/]+?)/$", url)
    store(url, r.group(1) + ".jpg")

def chandump(url, board):
    try:
        html = urllib.request.urlopen(url).read().decode("UTF-8")
        for u in re.findall("<a href=\"(//i.4cdn.org/" + board + "/([^/]+?)(.png|.jpg|.jpeg))\" target=\"_blank\">.+?</a>", html):
            store("https:" + u[0], u[1] + u[2])

    except urllib.error.HTTPError as err:
        if not err.code == 404:
            raise
