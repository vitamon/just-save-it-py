from google.appengine.ext import db
import logging

class SavedData(db.Model):
    app_id = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    jsoned_params = db.StringProperty()


def app_id_key(app_id=""):
    return db.Key.from_path('SavedData', app_id)


def persist(param):
    logging.debug("saving:", param)