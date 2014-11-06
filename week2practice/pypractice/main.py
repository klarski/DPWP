#Kristen Kozinski
#11/03/14
#Week 2 Practice

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        about_button.click()
        about_button.label = "About Us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact Us"
        contact_button.show_label()

class Button(object):
    def __init__(self):
        print "Constructor Method of button"
        self.click()
        self.label= "" #public attribute
        self.__size = 16 #private attribute
        self._color = "0x00000" #protected attribute
        #self.on_roll_over("Hello!!")

    def click(self):
        print "I've been clicked"

    def on_roll_over(self, message):
        print "I've been rolled over " + message

    def show_label(self):
        print "My label is " + self.label


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
