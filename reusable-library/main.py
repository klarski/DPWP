'''
Name: Kristen Kozinski
Date: 11/13/2014
Class: Design Patterns for Web Programming
Assignment: Reusable Library
'''

import webapp2
from pages import FormPage, ResultsPage
from lib import FormData, FormCal


class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = FormPage()
        data = FormData()
        lib = FormCal()
        results = ResultsPage()

        if self.request.GET:
            data.fname = self.request.GET['fname']
            data.lname = self.request.GET['lname']
            data.dob = self.request.GET['dob']
            data.username = self.request.GET['username']
            data.password = self.request.GET['password']
            data.ver_password = self.request.GET['verify-password']
            data.robot = self.request.GET['robot']

            data.dob = lib.age_check(data.dob)
            data.password = lib.password_match(data.password, data.ver_password)
            data.robot = lib.robot_check(data.robot)

            all = results.head + results.body + results.close
            all_answers = all.format(**locals())
            self.response.write(all_answers)
        else:
            self.response.write(f.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
