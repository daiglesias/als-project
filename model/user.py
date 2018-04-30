from google.appengine.ext import ndb


class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    expense = ndb.FloatProperty()
    added = ndb.DateProperty(auto_now_add=True, indexed=True)


def create(usr):
    new_user = User()

    new_user.email = usr.email()
    new_user.nick = usr.nickname()
    new_user.usr = usr

    return new_user


def update(user):
    return user.put()
