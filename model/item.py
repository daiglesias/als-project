from google.appengine.ext import ndb


class Item(ndb.Model):
    name = ndb.StringProperty(required=True)
    link = ndb.StringProperty()
    price = ndb.FloatProperty()
    owner = ndb.StringProperty(required=True)
    added = ndb.DateProperty(auto_now_add=True, indexed=True)
