from prometheus_client import start_http_server, Summary, Gauge
import time
from datetime import datetime
import sys
import random

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

g = Gauge('switch_linkstate_change', 'counts of link-up and down', ['zone', 'linkstate'])


# @g.track_inprogress()
# def f():
#     g.set(4.2)
#     g.set_to_current_time()

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
        # gauge_update(FLUSH)
