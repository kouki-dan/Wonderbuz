
import tornado.auth
from BaseHandler import BaseHandler


class AuthLoginHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
      #TODO
      pass

class AuthLogoutHandler(BaseHandler):
    def get(self):
      #TODO
      pass


