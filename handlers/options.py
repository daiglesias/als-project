import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2


class OptionHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        url_login = users.create_logout_url('/')
        user_name = user.nickname()
        logged = True

        jinja = jinja2.get_jinja2(app=self.app)
        valores = {"url_login": url_login, "logged": logged, "user_name": user_name}
        self.response.write(jinja.render_template('/options.html', **valores))


app = webapp2.WSGIApplication([
    ('/options', OptionHandler)
], debug=True)
