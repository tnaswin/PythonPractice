import sys
import csv
import urllib2
#import requests
from bs4 import BeautifulSoup
#from twisted.internet import reactor
#from twisted.internet import task, defer
#from twisted.web.client import getPage
#from twisted.python.util import println

countries = [
"af",
"al",
"dz",
"as",
"ad",
"ao",
"ai",
"aq",
"ag",
"ar",
"am",
"aw",
"au",
"at",
"az",
"bs",
"bh",
"bd",
"bb",
"by",
"be",
"bz",
"bj",
"bm",
"bt",
"bo",
"ba",
"bw",
"br",
"bn",
"bg",
"bf",
"bi",
"vg",
"kh",
"cm",
"ca",
"cv",
"bq",
"ky",
"cf",
"td",
"cl",
"cn",
"co",
"km",
"cg",
"ck",
"cr",
"ci",
"hr",
"cu",
"cw",
"cy",
"cz",
"dk",
"dj",
"dm",
"do",
"cd",
"ec",
"eg",
"sv",
"gq",
"er",
"ee",
"et",
"fk",
"fo",
"fj",
"fi",
"fr",
"gf",
"pf",
"ga",
"gm",
"ge",
"de",
"gh",
"gi",
"gr",
"gl",
"gd",
"gp",
"gu",
"gt",
"gn",
"gw",
"gy",
"ht",
"hn",
"hk",
"hu",
"is",
"in",
"id",
"ir",
"iq",
"ie",
"il",
"it",
"jm",
"jp",
"jo",
"kz",
"ke",
"ki",
"kw",
"kg",
"kp",
"kr",
"la",
"lv",
"lb",
"ls",
"lr",
"ly",
"li",
"lt",
"lu",
"mo",
"mk",
"mg",
"mw",
"my",
"mv",
"ml",
"mt",
"mh",
"mq",
"mr",
"mu",
"yt",
"mx",
"fm",
"md",
"mc",
"mn",
"me",
"ms",
"ma",
"mz",
"mm",
"na",
"nr",
"np",
"nl",
"nc",
"nz",
"ni",
"ne",
"ng",
"nu",
"no",
"om",
"pk",
"pw",
"ps",
"pa",
"pg",
"py",
"pe",
"ph",
"pl",
"pt",
"pr",
"qa",
"ro",
"ru",
"rw",
"re",
"sh",
"kn",
"pm",
"vc",
"ws",
"sm",
"st",
"sa",
"sn",
"rs",
"sc",
"sl",
"sg",
"sx",
"sk",
"si",
"sb",
"so",
"za",
"es",
"lk",
"sd",
"sr",
"sz",
"se",
"ch",
"sy",
"lc",
"ss",
"tw",
"tj",
"tz",
"th",
"tl",
"tg",
"tk",
"to",
"tt",
"tn",
"tr",
"tm",
"tc",
"tv",
"ug",
"ua",
"ae",
"gb",
"us",
"uy",
"uz",
"vi",
"vu",
"ve",
"vn",
"va",
"wf",
"ye",
"zm",
"zw"]
countries = ['zw']
for i in countries:
    i.upper()
    base_url="https://www.rebtel.com/en/rates/#{\"country\":\"%s\",\"currency\":\"USD\"}" %i
    #print base_url
    #page = urllib.request.urlopen(base_url)
    request_headers = {
"Accept-Language": "en-US,en;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Referer": "https://www.rebtel.com",
"Connection": "keep-alive"
}
    request = urllib2.Request(base_url, headers=request_headers)
    page = urllib2.urlopen(request).read()
    #request = urllib.request.Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
    #page = urllib.request.urlopen(request)
    #print page
    print "hello"
    soup = BeautifulSoup(page, 'html.parser')
    print(soup.prettify())
    """
    level1 = soup.find('display-row')
    #rows = table.find_all('li')
    level2 = soup.find("ul", {"class" : "custom-radio-list"})
    print "data is", repr(level2)
    level4 = soup.find_all("label", {"for" : "product-1000"})
    for l2 in level2:
        level3 = l.find_all('li')
        for l3 in level3:
            level4 = l3.find_all("label", {"for" : "product-1000"})
            level4=[x.text.strip() for x in l3]
            print level4
"""

"""
    title = soup.title
    date = title.string[:4]+','

    try:
        table = soup.find('product-worldcredit')
        rows = table.findAll('tr')
        for tr in rows:
            cols = tr.findAll('td')
            text_data = []
            for td in cols:
                text = ''.join(td)
                utftext = str(text.encode('utf-8'))
                text_data.append(utftext) # EDIT
            text = date+','.join(text_data)
    except:
        pass
"""
"""
    getPage(base_url).addCallbacks(
    callback=lambda value:(println(value),reactor.stop()),
    errback=lambda error:(println("an error occurred", error),reactor.stop()))

reactor.run()
"""
"""
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 for name, price in data:
   writer.writerow([name, price, datetime.now()])
"""
