from google.appengine.ext import ndb


class Item(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    link = ndb.StringProperty()
    price = ndb.FloatProperty()
    property = ndb.StringProperty(required=True)
