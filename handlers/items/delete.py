import webapp2
from google.appengine.ext import ndb


class AddItem(webapp2.RequestHandler):

    def post(self):
        item_id = self.request.get("item_id").strip()

        item = ndb.Key(urlsafe=item_id).get()
        item.key.delete()

        self.redirect("/items")


app = webapp2.WSGIApplication([
    ("/items/delete", AddItem),
], debug=True)
