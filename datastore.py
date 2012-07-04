from google.appengine.ext import db
import logging

class SavedData(db.Model):
    app_id = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    jsoned_params = db.StringProperty()


def app_id_key(app_id):
    return db.Key.from_path('SavedData', app_id)


def persist(params, app_id):
    logging.info("saving: %s" % params)
    data = SavedData(parent=app_id_key(app_id))
    data.app_id = app_id
    data.jsoned_params = params
    data.put()


def retrieve(app_id):
    data = db.GqlQuery("SELECT * FROM SavedData " +
                       "WHERE ANCESTOR IS :1 " +
                       "ORDER BY date DESC",
        app_id_key(app_id))
    return list(data)