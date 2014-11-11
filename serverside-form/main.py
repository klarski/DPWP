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
        f = Form()  # creating instance of Form class
        if self.request.GET:  # this if statement checks to see if the form is filled out and then gets the answers
            fname = self.request.GET['fname']  # first name input
            lname = self.request.GET['lname']  # last name input
            dob = self.request.GET['dob']  # date of birth input
            address = self.request.GET['address']  # address input
            city = self.request.GET['city']  # city input
            state = self.request.GET['state']  # state input
            zip = self.request.GET['zip']  # zip input
            idnum = self.request.GET['idnum']  # id number input
            party = self.request.GET['party']  # political party input
            age = self.request.GET['age']  # age radio button "yes" & "no input
            if age == "Yes":
                age = "You can vote on election day."
            else:
                age = "I'm sorry, you cannot vote on election day"
            all = f.head + f.body_page2 + f.close  # the all variable adds the form head, page2 view, & the form close
            all_answers = all.format(**locals())  # this puts all the form answers into the page 2 html
            self.response.write(all_answers)
        else:  # if form is not filled out the page1 view containing the form will show on page
            self.response.write(f.head + f.body + f.close)

# didn't touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
