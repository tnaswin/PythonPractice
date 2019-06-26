import sys
import csv
import urllib2
from bs4 import BeautifulSoup
from twisted.internet.defer import Deferred

countries = [
"afghanistan",
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
with open('bossrev.csv', 'w') as csv_file:
    for i in countries:
        base_url="https://www.bossrevolution.com/en-us/rates/%s" %i
        print "Base URL: ", base_url
        try:
            page = urllib2.urlopen(base_url)
        except:
            continue
        soup = BeautifulSoup(page, 'html.parser')
        #title = soup.title
        #print "Title: ", title
        table = soup.find('table')
        rows = table.find_all('tr')
        for tr in rows:
            cols = tr.find_all('td')
            text_data = []
            for td in cols:
                x = td.text.encode("utf-8")
                text_data.append(x)
                #print x
            #print "Data: ",text_data
            writer = csv.writer(csv_file)
            writer.writerow(text_data)
