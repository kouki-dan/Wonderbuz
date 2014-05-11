
import tornado.web
import os

from app.HomeHandler import HomeHandler
from app.AuthHandlers import AuthLoginHandler, AuthLogoutHandler
import secrets

class Application(tornado.web.Application):
  def __init__(self):
    handlers = [
        (r"/", HomeHandler),
        (r"/auth/login", AuthLoginHandler),
        (r"/auth/logout", AuthLogoutHandler),
        ]
    settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        cookie_secret=secrets.cookie_secret,
        login_url="/auth/login",
        debug=True,
        )
    tornado.web.Application.__init__(self, handlers, **settings)


