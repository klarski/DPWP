from datetime import datetime  # this is importing the date data from the datetime python library


class FormCal(object):
    def __init__(self):
        pass

# This method pulls the info entered into the date of birth field a checks to see if the user id 13 or older
    def age_check(self, d):
        date_format = "%Y-%m-%d" # set date format
        dob = datetime.strptime(d, date_format)  # reformat the date format pulled in from form
        current_date = datetime.today()  # gets the current date
        age = abs((current_date-dob).days)
        if int(age) >= (13*365):  # calclates to see if the user is old enough
            print "Yeah!, You are old enough"
            return str(d)
        else:
            return "You are not old enough"
        # Notes: check age entered into date field and see if user is over the age of 13

#this method checks to see if the two password fields match
    def password_match(self, p1, p2):
        print str(p1) + str(p2)
        if p1 == p2:
            return p1
        else:
            return "The passwords do not match"
        # Notes: check to see if password entered in password field matched password entered in the verify password field

#this method preforms a simple calculation based off the image in the form that verifies a human filled it out
    def robot_check(self, r):
        if int(r) == (3+1):
            print "You look legit"
            return r
        else:
            return "It looks like you might not be human"


class FormData(object):
    def __init__(self):
        self.__fname = ''
        self.__lname = ''
        self.__dob = 01/01/2014
        self.__username = ''
        self.__password = ''
        self.__ver_password = ''
        self.__robot = 0
# above sets up the attributes for the fields in the form- everything is set to private for encapsulating the form info

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, f):
        self.__fname = f


    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, l):
        self.__lname = l


    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, d):
        self.__dob = d


    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, u):
        self.__username = u


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, p):
        self.__password = p


    @property
    def ver_password(self):
        return self.__ver_password

    @ver_password.setter
    def ver_password(self, v):
        self.__ver_password = v


    @property
    def robot(self):
        return self.__robot

    @robot.setter
    def robot(self, r):
        self.__robot = r
