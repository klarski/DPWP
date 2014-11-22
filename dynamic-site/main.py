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

        p.coffee_buttons(c.blends_arr)

        print c.blends_arr[0].name
        print c.blends_arr[1].name
        print c.blends_arr[2].name
        print c.blends_arr[3].name
        print c.blends_arr[4].name

        if self.request.GET:
            name = self.request.GET['name']
            if name == 'Brooklyn Blend':
                p.product_view(c.blends_arr[0])
                self.response.write(p.print_out())
            else:
                print "Not working"
        else:
            self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
