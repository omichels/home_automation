import requests
from bs4 import BeautifulSoup
import os

# the class i'm interested in
school_class_to_watch = "07D"

contents = requests.get("http://www.riesener-gymnasium.de/vertretung/vertretung/schueler/heute.html")
soup = BeautifulSoup(contents.text, 'html.parser')

substitute = bool(0)
for td in soup.find_all('td',{"class":"klasse"}):
    if school_class_to_watch in td.string:  
        substitute = bool(1)


if substitute:
    # invoke android push nofication via notifymyandroid.com
    os.system('~/bin/nma.sh Vertretung Riesener ' + school_class_to_watch + ' 1')
else:
    print ("regular school today")


