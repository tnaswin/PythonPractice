import sys
import csv
import urllib2
from bs4 import BeautifulSoup
#from twisted.internet import task, defer
#from twisted.web.client import getPage
#from twisted.python.util import println
#from twisted.web.client import downloadPage

countries = ["afghanistan",
"albania",
"algeria",
"american-samoa",
"andorra",
"angola",
"anguilla",
"antarctica",
"antigua-and-barbuda",
"argentina",
"armenia",
"aruba",
"ascension-island",
"australia",
"austria",
"azerbaijan",
"bahamas",
"bahrain",
"bangladesh",
"barbados",
"belarus",
"belgium",
"belize",
"benin",
"bermuda",
"bhutan",
"bolivia",
"bosnia-and-herzegovina",
"botswana",
"brazil",
"british-virgin-islands",
"brunei-darussalam",
"bulgaria",
"burkina-faso",
"burundi",
"cambodia",
"cameroon",
"canada",
"cabo-verde",
"cayman-islands",
"central-african-republic",
"chad",
"chile",
"china",
"colombia",
"comoros",
"congo",
"cook-islands",
"costa-rica",
"croatia",
"cuba",
"cyprus",
"czech-republic",
"dr-congo",
"denmark",
"diego-garcia",
"djibouti",
"dominica",
"dominican-republic",
"TP",
"ecuador",
"egypt",
"el-salvador",
"equatorial-guinea",
"eritrea",
"estonia",
"ethiopia",
"falkland-islands",
"faroe-islands",
"fiji",
"finland",
"france",
"french-guiana",
"french-polynesia",
"gabon",
"gambia",
"georgia",
"germany",
"ghana",
"gibraltar",
"greece",
"greenland",
"grenada",
"guadeloupe",
"guam",
"guatemala",
"guinea",
"guinea-bissau",
"guyana",
"haiti",
"honduras",
"hong-kong",
"hungary",
"iceland",
"india",
"indonesia",
"iran",
"iraq",
"ireland",
"israel",
"italy",
"cote-d-ivoire",
"jamaica",
"japan",
"jordan",
"kazakhstan",
"kenya",
"kiribati",
"kuwait",
"kyrgyzstan",
"lao-people&#39;s-democratic-republic",
"latvia",
"lebanon",
"lesotho",
"liberia",
"libya",
"liechtenstein",
"lithuania",
"luxembourg",
"macao",
"macedonia",
"madagascar",
"malawi",
"malaysia",
"maldives",
"mali",
"malta",
"marshall-islands",
"mauritania",
"mauritius",
"mexico",
"micronesia",
"moldova",
"monaco",
"mongolia",
"montenegro",
"montserrat",
"morocco",
"mozambique",
"myanmar",
"namibia",
"nauru",
"nepal",
"netherlands",
"netherlands-antilles",
"new-caledonia",
"new-zealand",
"nicaragua",
"niger",
"nigeria",
"niue",
"northern-mariana-islands",
"north-korea",
"norway",
"oman",
"pakistan",
"palau",
"palestine",
"panama",
"papua-new-guinea",
"paraguay",
"peru",
"philippines",
"poland",
"portugal",
"puerto-rico",
"qatar",
"reunion",
"romania",
"russian-federation",
"rwanda",
"saint-martin-french",
"san-marino",
"sao-tome-and-principe",
"saudi-arabia",
"senegal",
"serbia",
"seychelles",
"sierra-leone",
"singapore",
"slovakia",
"slovenia",
"solomon-islands",
"somalia",
"south-africa",
"south-korea",
"south-sudan",
"spain",
"sri-lanka",
"saint-helena",
"saint-kitts-and-nevis",
"saint-lucia",
"saint-pierre-and-miquelon",
"saint-vincent-and-the-grenadines",
"sudan",
"suriname",
"swaziland",
"sweden",
"switzerland",
"syrian-arab-republic",
"taiwan",
"tajikistan",
"tanzania",
"thailand",
"togo",
"tokelau",
"tonga",
"trinidad-and-tobago",
"tunisia",
"turkey",
"turkmenistan",
"turks-and-caicos-islands",
"tuvalu",
"uganda",
"ukraine",
"united-arab-emirates",
"united-kingdom",
"uruguay",
"united-states",
"uzbekistan",
"vanuatu",
"venezuela",
"viet-nam",
"us-virgin-islands",
"wallis-and-futuna",
"samoa",
"yemen",
"zambia",
"zimbabwe"]
for i in countries:
    base_url="https://www.bossrevolution.com/en-us/rates/%s" %i
    print "Base URL: ", base_url
    try:
        page = urllib2.urlopen(base_url)
    except:
        continue
    print "page: ", page
    soup = BeautifulSoup(page, 'html.parser')
    #print "Soup: "
    #print(soup.prettify())
    title = soup.title
    #print "Title: ", title
    date = title.string[:4]+','
    print "Date: ", date
    table = soup.find('table')
    #print table
    rows = table.find_all('tr')
    with open('index.csv', 'w') as csv_file:
        for tr in rows:
            cols = tr.find_all('td')
            #print cols
            text_data = []
            for td in cols:
                #td = [x.text.strip() for x in td]
                x = td.text.encode("utf-8")
                text_data.append(x)
                #print text_data
                #print x
                #writer = csv.writer(csv_file)
                #writer.writerow(x)
                #writer.writerow(x.encode('utf-8'))
            #print "Hello: ",text_data
            writer = csv.writer(csv_file)
            writer.writerow(text_data)
            #utftext = [str(x).encode('latin-1') for x in td]
            #print utftext
            #text_data.append(utftext) # EDIT
        #text = date+','.join(text_data)
        #print text

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
