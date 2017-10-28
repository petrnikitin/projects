#import sys
#for i in sys.stdin:
#    print (line.split("")[0])
#    sys.stderr.write()



'''import json

a= """{
  "name": "Вася",       
  "surname": "Петров",
  "age": 35,           
  "isAdmin": false    
} """

d = json.loads(a)
print(d)
s = json.dumps(d, indent=4)
print (s)
'''

from bs4 import BeautifulSoup as BS
import requests


resp = requests.get("http://python.org")
soup = BS(resp.text, "lxml")

soup.find("h2", {"class": "widget-title"}).text
#soup.find("h2", {"align": "center"}).text
print (soup)

