import webapp2
import config
from pages import MainPage, GateWay

application_paths = [
    ('/', MainPage),
    ('/json', GateWay)
]

app = webapp2.WSGIApplication(application_paths, debug=config.debug_enabled)

