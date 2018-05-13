import urllib.request
import gzip
import json
import matplotlib.pyplot as plt
import datetime
import TokenPricePlot as token

url = "https://data.wowtoken.info/wowtoken.json"

request = urllib.request.Request(
    url,
    headers={
        "Accept-Encoding": "gzip"
    })

response = urllib.request.urlopen(request)
gzipFile = gzip.GzipFile(fileobj=response)
data = gzipFile.read()

my_json = data.decode('utf8').replace("'", '"')

file = open('wowtoken.txt', 'w')

file.write(my_json)

token = token.WowPlot()

ex = True

while(ex):
    option = input('\n1. EU (Europe)\n2. NA (North America)\n3. CN (China)\n4. TW (Taiwan)\n5. KR (Korea)\nPress any to EXIT\n\n')
    if(option=='1'):
        token.getGraphByRegion('EU')
    elif(option=='2'):
        token.getGraphByRegion('NA')
    elif(option=='3'):
        token.getGraphByRegion('CN')
    elif(option=='4'):
        token.getGraphByRegion('TW')
    elif(option=='5'):
        token.getGraphByRegion('KR')
    else:
        ex = False