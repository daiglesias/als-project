from google.appengine.ext import ndb


class Auction(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    link = ndb.StringProperty()
    normal_price = ndb.FloatProperty()
    wanted_price = ndb.FloatProperty()
    risk = ndb.FloatProperty()
    final_price = ndb.FloatProperty()
    state = ndb.BooleanProperty()
    property = ndb.StringProperty(required=True)
