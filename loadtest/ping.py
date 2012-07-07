import string
from httplib2 import Http
from urllib import urlencode
import random

h = Http()
#main_url = "http://localhost:8080/save"
main_url = "http://just-save-it-py.appspot.com/save"

def generateParams():
    result = ''
    num_params = random.randint(1, 20)
    for p in xrange(num_params):
        len = random.randint(1, 16)
        result += "p%s=" % p + "".join(random.choice(string.letters + "0123456789") for i in xrange(len)) + "&"
    return result[:-1]

data = "APP_ID=ldt&%s" % generateParams()

#data = r"APP_ID=ldt&p0=wJoKVmJDcPVtFI&p1=bg&p2=EnZyKl&p3=qtooWb86WpvkKz&p4=4eoP&p5=ZNc&p6=ldKLtnhV7oRtf"
#data = dict(APP_ID="asd", comment="A test comment")
resp, content = h.request(main_url, "POST", data)

print resp

