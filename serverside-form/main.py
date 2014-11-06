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
        f = Form()
        if self.request.GET:
            fname = self.request.GET['fname']
            lname = self.request.GET['lname']
            dob = self.request.GET['dob']
            address = self.request.GET['address']
            city = self.request.GET['city']
            state = self.request.GET['state']
            zip = self.request.GET['zip']
            idnum = self.request.GET['idnum']
            party = self.request.GET['party']
            age = self.request.GET['age']
            if age == "Yes":
                age = "You can vote on election day."
            else:
                age = "I'm sorry, you cannot vote on election day"
            all = f.head + f.body_page2 + f.close
            all_answers = all.format(**locals())
            self.response.write(all_answers)
        else:
            self.response.write(f.head + f.body + f.close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
