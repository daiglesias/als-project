import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb

from model.auction import Auction


class AddAuction(webapp2.RequestHandler):

    def post(self):
        name = self.request.get("name", "").strip()
        link = self.request.get("link", "").strip()
        auction_id = self.request.get("auction_id", "").strip()
        normal_price = float(self.request.get("normal_price", 0.0).strip())
        wanted_price = float(self.request.get("wanted_price", 0.0).strip())
        risk = float(self.request.get("risk", 0.0).strip())
        final_price = float(self.request.get("final_price", 0.0).strip())
        owner = users.get_current_user().user_id()

        if link and not link.startswith("http://") and not link.startswith("https://"):
            link = "http://" + link

        if auction_id:
            auction = ndb.Key(urlsafe=auction_id).get()
            auction.name = name
            auction.link = link
            auction.normal_price = normal_price
            auction.wanted_price = wanted_price
            auction.risk = risk
            auction.final_price = final_price
        else:
            auction = Auction(name=name,
                              link=link,
                              normal_price=normal_price,
                              wanted_price=wanted_price,
                              risk=risk,
                              final_price=final_price,
                              owner=owner)
        auction.put()
        self.redirect("/auctions")


app = webapp2.WSGIApplication([
    ("/auctions/add", AddAuction),
], debug=True)
