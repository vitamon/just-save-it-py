"""Simple web application load testing script.
"""
import string
from unicodedata import digit

import httplib2
import random
import socket
import time
from threading import Event
from threading import Thread
from threading import current_thread
from urllib import urlencode

# Modify these values to control how the testing is done

# How many threads should be running at peak load.
NUM_THREADS = 10

# How many minutes the test should run with all threads active.
TIME_AT_PEAK_QPS = 10 # minutes

# How many seconds to wait between starting threads.
# Shouldn't be set below 30 seconds.
DELAY_BETWEEN_THREAD_START = 30 # seconds

quitevent = Event()

#main_url = "http://localhost:8080/save"
main_url = "http://just-save-it-py.appspot.com/save"

def generateParams():
    d = dict()
    d["APP_ID"] = "LoadTest1"
    num_params = random.randint(1, 20)
    for p in xrange(num_params):
        len = random.randint(1, 16)
        d["p%s" % str(p)] = "".join(random.choice(string.letters + "0123456789") for i in xrange(len))
    return urlencode(d)


def threadproc():
    """This function is executed by each thread."""
    print "Thread started: %s" % current_thread().getName()
    h = httplib2.Http(timeout=30)
    while not quitevent.is_set():
        try:
            # HTTP requests to exercise the server go here
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            url = generateParams()
            print url
            resp, content = h.request(main_url, "POST", url)
            print resp
            if resp.status != 202:
                print "Response not OK"
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        except socket.timeout:
            pass

    print "Thread finished: %s" % current_thread().getName()

if __name__ == "__main__":
    runtime = (TIME_AT_PEAK_QPS * 60 + DELAY_BETWEEN_THREAD_START * NUM_THREADS)
    print "Total runtime will be: %d seconds" % runtime
    threads = []
    try:
        for i in range(NUM_THREADS):
            t = Thread(target=threadproc)
            t.start()
            threads.append(t)
            time.sleep(DELAY_BETWEEN_THREAD_START)
        print "All threads running"
        time.sleep(TIME_AT_PEAK_QPS * 60)
        print "Completed full time at peak qps, shutting down threads"
    except:
        print "Exception raised, shutting down threads"

    quitevent.set()
    time.sleep(3)
    for t in threads:
        t.join(1.0)
    print "Finished"