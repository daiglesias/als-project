import webapp2
from google.appengine.api import users
from model.item import Item
from webapp2_extras import jinja2

class AddItem(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app = self.app)
        values = {} # Valores

        self.response.write(jinja.render_template("newItem.html", **values))

    def post(self):

        name = self.request.get("name", "").strip()
        description = self.request.get("description", "").strip()
        link = self.request.get("link", "").strip()
        price = self.request.get("price", "").strip()
        property = self.request.get("property", "").strip()

        item = item(name = name, description = description, link = link, price = price, property = property)
        item.put()
        self.redirect("/")


app = webapp2.WSGIApplication([
    ("/items/add", AddItem),
], debug=True)
