import urllib.request
import gzip
import json
import TokenPricePlot

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

ex = True

token = TokenPricePlot.WowPlot()
while(ex):
    option = input('1. EU\n2. NA\n3. CN\nPress any to EXIT\n\n')
    if(option=='1'):
        token.getGraphByRegion('EU')
    elif(option=='2'):
        token.getGraphByRegion('NA')
    elif(option=='3'):
        token.getGraphByRegion('CN')
    else:
        ex = False