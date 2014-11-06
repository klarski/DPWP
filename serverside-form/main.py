'''
Name: Kristen Kozinski
Date: 11/05/2014
Class: Design Patterns for Web Programming
Assignment: Lab 2 Server Side Form
'''

import webapp2
from pages import Form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = Form()
        self.response.write(f.head + f.body + f.close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
