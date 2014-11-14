'''
Name: Kristen Kozinski
Date: 11/13/2014
Class: Design Patterns for Web Programming
Assignment: Reusable Library

The Kimpmail name was inspired by the MailChimp ad for the Serial radio show and all the different ways people will
refer to MailChimp when writing into support (chimpmail, monkeymail, etc). I am hopping to build out this idea further
after the class is over as a unique portfolio piece to show our dev team.
Read more about that here: http://mashable.com/2014/11/12/marchimp-mailkimp-meme/?utm_cid=mash-com-fb-main-link
'''

import webapp2
from pages import FormPage, ResultsPage
from lib import FormData, FormCal


class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = FormPage()  # creating instance of FormPage class
        data = FormData()  # creating instance of FormData class
        lib = FormCal()  # creating instance of FormCal class
        results = ResultsPage()  # creating instance of ResultsPage class

        if self.request.GET:  # this if statement checks to see if the form is filled out and then gets the answers
            data.fname = self.request.GET['fname']  # first name input
            data.lname = self.request.GET['lname']  # last name input
            data.dob = self.request.GET['dob']  # Date of birth input
            data.username = self.request.GET['username']  # username input
            data.password = self.request.GET['password']  # password input
            data.ver_password = self.request.GET['verify-password'] # verify password input
            data.robot = self.request.GET['robot']  # Human validation input

            data.dob = lib.age_check(data.dob)  # calls age-check method in lib & passes DOB data to validate age
            data.password = lib.password_match(data.password, data.ver_password)  # calls password_match in lib
            data.robot = lib.robot_check(data.robot)  # calls robot_check in lib

            all = results.head + results.body + results.close  # adds all pieces of html file on ResultsPage class
            all_answers = all.format(**locals())  # pushes form values into html code
            self.response.write(all_answers)  # writes it all to the page
        else:
            self.response.write(f.print_out())  # if form is not filled out only form will display


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
