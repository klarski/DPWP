from datetime import datetime


class FormCal(object):
    def __init__(self):
        pass

    def age_check(self, d):
        date_format = "%Y-%m-%d"
        dob = datetime.strptime(d, date_format)
        current_date = datetime.today()
        age = abs((current_date-dob).days)
        if int(age) >= (13*365):
            print "Yeah!, You are old enough"
            return d
        else:
            print "You are not old enough"

        # check age entered into date field and see if user is over the age of 13
    def password_match(self, p1, p2):
        print str(p1) + str(p2)
        if p1 == p2:
            return p1
        else:
            print "The passwords do not match"
        #check to see if password entered in password field matched password entered in the verify password field

    def robot_check(self, r):
        if int(r) == (3+1):
            print "You look legit"
            return r
        else:
            print "It looks like you might not be human"


class FormData(object):
    def __init__(self):
        self.fname = ''
        self.lname = ''
        self.dob = 01/01/1900
        self.username = ''
        self.password = ''
        self.ver_password = ''