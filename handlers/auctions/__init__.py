import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2

from model.auction import Auction

class AuctionHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()


        jinja = jinja2.get_jinja2(app=self.app)
        valores = {}
        self.response.write(jinja.render_template('/auctions.html', **valores))


app = webapp2.WSGIApplication([
    ('/auctions', AuctionHandler)
], debug=True)
