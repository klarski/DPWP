'''
Name: Kristen Kozinski
Date: 11/20/2014
Class: Design Patterns for Web Programming
Assignment: Dynamic Site

My project is based on a store for a fictional company that I created called Handsome Hipster Coffee Roasters. I have created projects for past classes for Handsome Hipster Coffee Roasters. The only thing borrowed from the past project was the brand assets (logo and branding styles- ie font styles and colors).
'''

import webapp2
from data import CoffeeTypes  # importing CoffeeTypes class from data.py
from pages import ContentPage  # importing ContentPage class from pages.py


class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = ContentPage()  # creating instance of ContentPage class
        c = CoffeeTypes()  # creating instance of CoffeeTypes class

        p.coffee_buttons(c.blends_arr)  # this function is located in Content pages. I am calling it here and passing my coffee blends array into the function

        #  these GET requests are looking at my "buttons" on pages.py and saying if it is clicked, run product_view function and pass the coffee blends array into the function
        if self.request.GET:
            name = self.request.GET['name']  # getting the name from my buttons set up in pages.py under coffee_buttons
            if name == 'Brooklyn Blend':  # if the name is Brooklyn Blend, it is pushing the brooklyn blend data object into the product_view function and printing the page
                p.product_view(c.blends_arr[0])
                self.response.write(p.print_out())
            if name == 'Portland Blend':  # if the name is Portland Blend, it is pushing the portland blend data object into the product_view function and printing the page
                p.product_view(c.blends_arr[1])
                self.response.write(p.print_out())
            if name == 'Austin Blend':  # if the name is Austin Blend, it is pushing the austin blend data object into the product_view function and printing the page
                p.product_view(c.blends_arr[2])
                self.response.write(p.print_out())
            if name == 'Boston Blend':  # if the name is Boston Blend, it is pushing the boston blend data object into the product_view function and printing the page
                p.product_view(c.blends_arr[3])
                self.response.write(p.print_out())
            if name == 'SanFran Blend':  # if the name is SanFran Blend, it is pushing the sanfran blend data object into the product_view function and printing the page
                p.product_view(c.blends_arr[4])
                self.response.write(p.print_out())
            else:
                print "Not working"
        else:
            self.response.write(p.print_out())  # if it cannot GET name, page will just be printed


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
