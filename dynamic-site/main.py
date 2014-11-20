'''
Name: Kristen Kozinski
Date: 11/20/2014
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

import webapp2
from data import *
from pages import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        c = CoffeeTypes()
        bb = BrooklynBlend()

        bb.name = self.request.GET['name']
        c.coffee_values(bb)


        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
