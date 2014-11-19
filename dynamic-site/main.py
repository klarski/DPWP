'''
Name: Kristen Kozinski
Date: 11/20/2014
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
