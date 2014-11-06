import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        abed = Character()
        abed.name = "Abed Nadir"
        abed.profession = "student"
        abed.fav_class = "Anthropology"
        abed.age = 24

        annie = Character()
        annie.name = "Annie Edison"
        annie.profession = "student"
        annie.fav_class = "Spanish"
        annie.age = 22

        jeff = Character()
        jeff.name = "Jeff Winger"
        jeff.profession = "teacher"
        jeff.fav_class = "Pottery"
        jeff.age = 35

        chars = [abed, annie, jeff]
        print chars[1].fav_class

class Character(object):
    def __init__(self):
        self.name = ""
        self.profession = ""
        self.fav_class = ""
        self.age = ""

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
