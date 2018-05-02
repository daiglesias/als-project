import webapp2
from google.appengine.ext import ndb


class DeleteAuction(webapp2.RequestHandler):

    def post(self):
        auction_id = self.request.get("auction_id").strip()

        auction = ndb.Key(urlsafe=auction_id).get()
        auction.key.delete()

        self.redirect("/auctions")


app = webapp2.WSGIApplication([
    ("/auctions/delete", DeleteAuction),
], debug=True)
