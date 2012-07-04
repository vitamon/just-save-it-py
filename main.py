import webapp2
import config
from handlers import IndexPage, GateWay

application_paths = [
    ('/', IndexPage),
    ('/json', GateWay)
]

app = webapp2.WSGIApplication(application_paths, debug=config.debug_enabled)

