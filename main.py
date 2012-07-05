import webapp2
import config
from handlers import IndexPage, Preview, Save, JsonEndpoint

application_paths = [
    ('/', IndexPage),
    ('/save', Save),
    ('/preview', Preview),
    ('/json', JsonEndpoint)
]

app = webapp2.WSGIApplication(application_paths, debug=config.debug_enabled)

