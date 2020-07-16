from datetime import datetime, timedelta

import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2

from model.auction import Auction
from model.item import Item


class ExpensesHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        url_login = users.create_logout_url('/')

        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                  "Noviembre", "Diciembre"]
        end_time = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        start_time = end_time - timedelta(weeks=1)

        expenses = {}
        items = Item.query(Item.owner == users.get_current_user().user_id(), Item.added > start_time).order(-Item.added)

        for item in items:
            year = item.added.year
            month = months[item.added.month - 1]

            if year not in expenses:
                expenses[year] = {}
            if month not in expenses[year]:
                expenses[year][month] = 0

            expenses[year][month] += item.price

        auctions = Auction.query(Auction.owner == users.get_current_user().user_id(), Auction.added > start_time).order(
            -Auction.added)

        for auction in auctions:
            year = auction.added.year
            month = months[auction.added.month - 1]

            if year not in expenses:
                expenses[year] = {}
            if month not in expenses[year]:
                expenses[year][month] = 0

            expenses[year][month] += auction.final_price

        jinja = jinja2.get_jinja2(app=self.app)
        values = {"url_login": url_login, "user": user, "expenses": expenses}
        self.response.write(jinja.render_template('/expenses.html', **values))


app = webapp2.WSGIApplication([
    ('/expenses', ExpensesHandler)
], debug=True)
