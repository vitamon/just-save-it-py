import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
import appmodel, datastore

class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(self, filename, **template_args):
        self.response.write(self.jinja2.render_template(filename, **template_args))


class IndexPage(BaseHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.render_template('index.html', **{"name": user.nickname()})
        else:
            self.redirect(users.create_login_url(self.request.uri))


class BaseGetHandler(BaseHandler):
    def get(self):
        params = self.request.GET

        if not appmodel.valid(**params):
            self.response.set_status(400, "No APP_ID provided")
            return

        data = datastore.retrieve(appmodel.get_id(**params))
        self.process(data)

    def process(self, data):
        pass


class Preview(BaseGetHandler):
    def process(self, data):
        self.render_template('params.html', **{'params': data})


class JsonEndpoint(BaseGetHandler):
    def process(self, data):
        self.response.content_type = 'application/json'
        self.response.write(appmodel.list_as_json(data))



class Save(BaseHandler):
    def post(self):
        params = self.request.POST

        if not appmodel.valid(**params):
            self.response.set_status(400, "No APP_ID provided")
            return

        datastore.persist(appmodel.as_json(**params), appmodel.get_id(**params))
        self.response.set_status(202)
