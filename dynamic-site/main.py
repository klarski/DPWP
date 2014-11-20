'''
Name: Kristen Kozinski
Date: 11/20/2014
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

import webapp2
from data import CoffeeTypes

class MainHandler(webapp2.RequestHandler):
    def get(self):
        c = CoffeeTypes()
        self.response.write("Test")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
