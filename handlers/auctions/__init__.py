import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2

from model.auction import Auction


class AuctionHandler(webapp2.RequestHandler):

    def get(self):
        auctions = Auction.query(Auction.owner == users.get_current_user().user_id()).order(-Auction.added)

        jinja = jinja2.get_jinja2(app=self.app)
        valores = {"auctions": auctions}
        self.response.write(jinja.render_template('/auctions.html', **valores))


app = webapp2.WSGIApplication([
    ('/auctions', AuctionHandler)
], debug=True)
