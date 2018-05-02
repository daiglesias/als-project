import webapp2
from google.appengine.api import users
from model.item import Item


class AddItem(webapp2.RequestHandler):

    def post(self):
        name = self.request.get("name", "").strip()
        link = self.request.get("link", "").strip()
        price = float(self.request.get("price", 0.0).strip())
        owner = users.get_current_user().user_id()

        item = Item(name=name, link=link, price=price, owner=owner)
        item.put()
        self.redirect("/items")


app = webapp2.WSGIApplication([
    ("/items/add", AddItem),
], debug=True)
