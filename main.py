#!/usr/bin/env python

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        stran = open("index.html")
        return self.response.write(stran.read())

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
