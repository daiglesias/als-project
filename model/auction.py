from google.appengine.ext import ndb


class Auction(ndb.Model):
    name = ndb.StringProperty(required=True)
    link = ndb.StringProperty()
    normal_price = ndb.FloatProperty()
    wanted_price = ndb.FloatProperty()
    risk = ndb.FloatProperty()
    final_price = ndb.FloatProperty()
    owner = ndb.StringProperty(required=True)
    added = ndb.DateProperty(auto_now_add=True, indexed=True)

