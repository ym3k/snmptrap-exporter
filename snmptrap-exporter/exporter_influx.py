from prometheus_client import start_http_server, Gauge
import influxdb
import time
from datetime import datetime
import sys

DBHOST='influxdb'
DBPORT=8086
DBNAME='switch'
COLLECTIONNAME='snmptrap'
USER="root"
PASS="root"
FLUSH = 10 # in sec
INTERVAL = 30 #

labelkey = ['zone', 'hostname', 'interface', 'linkstate']

# connect to influxdb
class influxConnect(object):
    def __init__(self, dbhost=DBHOST, port=DBPORT, 
                 dbname=DBNAME, collection=COLLECTIONNAME, 
                 user=USER, password=PASS):
        client = influxdb.InfluxDBClient(host=dbhost, port=port, username=user, password=password)
        client.switch_database(dbname)
        self.client = client
        self.querystr = 'SELECT * FROM "{0}" WHERE time > now() - {1}s'.format(COLLECTIONNAME,INTERVAL)
        self.gauges = set()
        

    def last_state_change2(self):
        value = {key: 0 for key in self.gauges}
        resultset = self.client.query(self.querystr)
        # with open("/tmp/aaa", 'a') as f:
        #     print(datetime.fromtimestamp(time.time()),resultset, file=f)
        for i in resultset.get_points():
            key = "_".join([i[k] for k in labelkey])
            if key in value:
                value[key] += 1
            else:
                value[key] =  1
                self.gauges.add(key)
        return value


g = Gauge('switch_linkstate_change', 'counts of link-up and down', labelkey)

co = influxConnect()


def gauge_update(waittime):
    a = co.last_state_change2()
    for mykey, myvalue in a.items():
        (z, h, i, l) = mykey.split("_")
        g.labels(z, h ,i, l).set(myvalue)
    time.sleep(waittime)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        gauge_update(FLUSH)
