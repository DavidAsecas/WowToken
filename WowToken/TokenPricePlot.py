import json
import matplotlib.pyplot as plot
import datetime

class WowPlot():
    timestamp = []
    price = []
    date = []
    f = plot.Figure()

    def getGraphByRegion(self,region):
        with open('wowtoken.txt') as json_file:  
            data = json.load(json_file)

        for priceList in data['history'][str(region)]:
            self.timestamp.append(priceList[0])
            self.price.append(priceList[1])

        self.date = [datetime.datetime.fromtimestamp(time) for time in self.timestamp]
        graph = self.f.add_subplot(111)
        graph.clear()
        graph.plot(self.date,self.price)

    def clearPlot(self): 
        plot.clf()