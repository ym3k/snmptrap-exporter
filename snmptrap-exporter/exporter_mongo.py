from prometheus_client import start_http_server, Gauge
from pymongo import MongoClient
import time
from datetime import datetime

DBHOST='mongo'
DBPORT=27017
DBNAME='fluentd'
COLLECTIONNAME='snmptrap'
FLUSH = 10 # in sec
INTERVAL = 30 #

labelkey = ['zone', 'hostname', 'interface', 'linkstate']

# connect to MongoDB
class MongoConnect(object):
    
    def __init__(self, dbhost=DBHOST, port=DBPORT, dbname=DBNAME, collection=COLLECTIONNAME):
        client = MongoClient(dbhost, port)
        db = client[dbname]
        self.collection = db[COLLECTIONNAME]
        self.gauges = set()

    def current_period(self):
        now = time.time() 
        # now = time() // DELAY * DELAY
        self.to_datetime = datetime.fromtimestamp(now)
        self.from_datetime = datetime.fromtimestamp(now - INTERVAL)

    # def last_state_change(self):
    #     self.current_period()
    #     period = { "$and": [ {"time": { "$gte": self.from_datetime }}, 
    #                          {"time": { "$lt":  self.to_datetime   }} ] }
        
    #     lschanges = self.collection.aggregate([{ "$match": period}, self.group_link_zone])
    #     return [i for i in lschanges]

    def last_state_change2(self):
        self.current_period()
        period = { "$and": [ {"time": { "$gte": self.from_datetime }}, 
                             {"time": { "$lt":  self.to_datetime   }} ] }
        value = {key: 0 for key in self.gauges}
        for i in self.collection.find(period):
            key = "_".join([i[k] for k in labelkey])
            if key in value:
                value[key] += 1
            else:
                value[key] =  1
                self.gauges.add(key)
        return value



g = Gauge('switch_linkstate_change', 'counts of link-up and down', labelkey)

co = MongoConnect()


def gauge_update(waittime):
    a = co.last_state_change2()
    for mykey, myvalue in a.items():
        (z, h, i, l) = mykey.split("_")
        g.labels(z, h, i, l).set(myvalue)
    time.sleep(waittime)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        gauge_update(FLUSH)
