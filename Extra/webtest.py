import requests
from bs4 import BeautifulSoup
import pandas

base_url = "https://www.bossrevolution.com/en-us/rates/mexico"
r = requests.get(base_url)
c = r.content

soup = BeautifulSoup(c,"html.parser")

paging = soup.find("input",{"id":"placardContainer"}).find("input",{"id":"ratesel_data"}).find_all("a")
start_page = paging[1].text
last_page = paging[len(paging)-2].text

"""
f = open('data.txt','w')
for i in countries:
    base_url="https://www.bossrevolution.com/en-us/rates/%s" %i
    #print base_url
    try:
        page = urllib2.urlopen(base_url)
    except:
        continue
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.title
    date = title.string[:4]+','

    try:
        table = soup.find('table')
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
f.close()
"""
