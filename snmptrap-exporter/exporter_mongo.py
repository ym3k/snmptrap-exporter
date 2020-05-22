from prometheus_client import start_http_server, Summary, Gauge
from pymongo import MongoClient
# import random
import time
from datetime import datetime

DBHOST='mongo'
DBPORT=27017
DBNAME='fluentd'
COLLECTIONNAME='snmptrap'
DELAY = 60 # in sec

# connect to MongoDB
class MongoConnect(object):
    
    def __init__(self, dbhost=DBHOST, port=DBPORT, dbname=DBNAME, collection=COLLECTIONNAME):
        client = MongoClient(dbhost, port)
        db = client[dbname]
        self.collection = db[COLLECTIONNAME]
        self.zone_link = []
        self.group_link_zone = { 
            "$group" : { 
                "_id" : { "zone": "$zone", "linkstate": "$linkstate"} ,
                "count" : { "$sum" : 1  } 
            }}
    def current_period(self):
        now = time.time() 
        # now = time() // DELAY * DELAY
        self.to_datetime = datetime.fromtimestamp(now)
        self.from_datetime = datetime.fromtimestamp(now - DELAY)

    def last_state_change(self):
        self.current_period()
        period = { "$and": [ {"time": { "$gte": self.from_datetime }}, 
                             {"time": { "$lt":  self.to_datetime   }} ] }
        
        lschanges = self.collection.aggregate([{ "$match": period}, self.group_link_zone])
        return [i for i in lschanges]

    def last_state_change2(self):
        self.current_period()
        period = { "$and": [ {"time": { "$gte": self.from_datetime }}, 
                             {"time": { "$lt":  self.to_datetime   }} ] }
        value = {key: 0 for key in self.zone_link}
        for i in self.collection.find(period):
            key = "_".join([i['zone'], i['linkstate']])
            if key in value:
                value[key] += 1
            else:
                value[key] =  1
                self.zone_link.append(key)
        return value


# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

g = Gauge('switch_linkstate_change', 'counts of link-up and down', ['zone', 'linkstate'])


# @g.track_inprogress()
# def f():
#     g.set(4.2)
#     g.set_to_current_time()

co = MongoConnect()


# def gauge_update(waittime):
#     lschanges = co.last_state_change()
#     for i in lschanges:
#         (labels, count) = i.values()
#         g.labels(labels['zone'], labels['linkstate']).set(count)
#     time.sleep(waittime)

def gauge_update(waittime):
    a = co.last_state_change2()
    for mykey, myvalue in a.items():
        (zone, linkstate) = mykey.split("_")
        g.labels(zone, linkstate).set(myvalue)
        # g.labels('zoneA', mykey).set(myvalue)
    time.sleep(waittime)

# Decorate function with metric.
# @REQUEST_TIME.time()
# def process_request(t):
#     """A dummy function that takes some time."""
#     time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        # process_request(random.random())
        gauge_update(DELAY)
