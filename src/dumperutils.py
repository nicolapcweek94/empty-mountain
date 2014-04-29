import urllib.request, re

def store(name, url):
    print("[~] Downloading " + url + " -> " + name)
    f = urllib.request.urlopen(url)
    with open(name, "b+w") as g:
        g.write(f.read())

def imguralbum(url):
    html = urllib.request.urlopen(url).read().decode("UTF-8")
    for s in re.findall("<a.+?class=\"zoom\".+?href=\"(.+?)\">", html):
        r = re.search("([^/]+?)(.png|.jpg|.jpeg)$", s)
        store(r.group(1) + r.group(2), "https:" + s)

def imgursingle(url):
    html = urllib.request.urlopen(url).read().decode("UTF-8")
    r = re.search("<a.+?href=\".+?/([^/]+?)(.png|.jpg|.jpeg)\">", html)
    store(r.group(1) + r.group(2), url)

def steamscreen(url):
    r = re.search(".+?/([^/]+?)/$", url)
    store(r.group(1) + ".jpg", url)
