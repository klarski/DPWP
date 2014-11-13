
class FormCal(object):
    def __init__(self):
        pass

    def age_check(self, d):
        print d
        # check age entered into date field and see if user is over the age of 13

    def password_match(self, p1, p2):
        print str(p1) + str(p2)
        if p1 == p2:
            return p1
        else:
            print "The passwords do not match"
        #check to see if password entered in password field matched password entered in the verify password field


class FormData(object):
    def __init__(self):
        self.fname = ''
        self.lname = ''
        self.dob = 01/01/1900
        self.username = ''
        self.password = ''
        self.ver_password = ''