'''
Name: Kristen Kozinski
Date: 11/13/2014
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

import webapp2
from pages import FormPage


class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = FormPage()
        self.response.write(f.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
