'''
Name: Kristen Kozinski
Date: 11/20/2014
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
'''

import webapp2
from data import CoffeeTypes
from pages import ContentPage


class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = ContentPage()
        c = CoffeeTypes()

        if self.request.GET:
            name == self.request.GET['name']
                if name == 'Brooklyn Blend':
                    p.product_view()
                else:
                    pass
        else:
            pass

        p.coffee_buttons(c.blends_arr)
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
