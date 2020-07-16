import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2


class OptionHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        url_login = users.create_logout_url('/')

        jinja = jinja2.get_jinja2(app=self.app)
        values = {"url_login": url_login, "user": user}
        self.response.write(jinja.render_template('/options.html', **values))


app = webapp2.WSGIApplication([
    ('/options', OptionHandler)
], debug=True)
