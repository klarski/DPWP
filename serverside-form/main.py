'''
Name: Kristen Kozinski
Date: 11/05/2014
Class: Design Patterns for Web Programming
Assignment: Lab 2 Server Side Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
