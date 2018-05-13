import json
import matplotlib.pyplot as plt
import datetime

class WowPlot():

    def getGraphByRegion(self,region):
        timestamp = []
        price = []
        date = []
        with open('wowtoken.txt') as json_file:  
            data = json.load(json_file)

        for priceList in data['history'][str(region)]:
            timestamp.append(priceList[0])
            price.append(priceList[1])

        date = [datetime.datetime.fromtimestamp(time) for time in timestamp]

        plt.close('all')
        f, ax = plt.subplots()
        ax.plot(date,price)
        ax.set_title(region)
        plt.show()