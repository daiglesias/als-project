import webapp2
from google.appengine.api import users
from model.auction import Auction
from webapp2_extras import jinja2


class AddAuction(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        values = {}  # Valores

        self.response.write(jinja.render_template("add_auction.html", **values))

    def post(self):
        name = self.request.get("name", "").strip()
        link = self.request.get("link", "").strip()
        normal_price = self.request.get("normal_price", "").strip()
        wanted_price = self.request.get("wanted_price", "").strip()
        risk = self.request.get("risk", "").strip()
        final_price = self.request.get("final_price", "").strip()
        state = self.request.get("state", "").strip()
        owner = self.request.get("owner", "").strip()

        auction = Auction(name=name,
                          link=link,
                          normal_price=normal_price,
                          wanted_price=wanted_price,
                          risk=risk,
                          final_price=final_price,
                          state=state,
                          owner=owner)
        auction.put()
        self.redirect("/")


app = webapp2.WSGIApplication([
    ("/auctions/add", AddAuction),
], debug=True)
