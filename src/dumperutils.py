import urllib.request, re

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
    store(url, r.group(1) + r.group(2))

def steamscreen(url):
    r = re.search(".+?/([^/]+?)/$", url)
    store(url, r.group(1) + ".jpg")
