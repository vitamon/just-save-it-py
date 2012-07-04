import webapp2
from webapp2_extras import jinja2

class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(self, filename, **template_args):
        self.response.write(self.jinja2.render_template(filename, **template_args))

class IndexPage(BaseHandler):
    def get(self):
        self.render_template('index.html', **{})

class GateWay(BaseHandler):
    def get(self):
        params = self.request.GET
        self.render_template('params.html', **{'params': params})

    def post(self):
        params = self.request.POST
        #do save to db

