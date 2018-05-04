import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb

from model.item import Item


class AddItem(webapp2.RequestHandler):

    def post(self):
        name = self.request.get("name", "").strip()
        item_id = self.request.get("item_id", "").strip()
        link = self.request.get("link", "").strip()
        price = float(self.request.get("price", 0.0).strip())
        owner = users.get_current_user().user_id()

        if link and not link.startswith("http://") and not link.startswith("https://"):
            link = "http://" + link

        if item_id:
            item = ndb.Key(urlsafe=item_id).get()
            item.name = name
            item.link = link
            item.price = price
        else:
            item = Item(name=name, link=link, price=price, owner=owner)
        item.put()
        self.redirect("/items")


app = webapp2.WSGIApplication([
    ("/items/add", AddItem),
], debug=True)
