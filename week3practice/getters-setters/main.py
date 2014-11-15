
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        t = Transcripts()
        t.grade1 = 90
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 78
        t.final_grade = 99
        self.response.write("Tommy's final grade is: " + str(t.final_grade))

        s = Transcripts()
        s.grade1 = 94
        s.grade2 = 89
        s.quiz1 = 66
        s.quiz2 = 70
        s.calc_grade()
        self.response.write(</br>"Sally's final grade is: " + str(s.final_grade))

class Transcripts():
    def __init__(self):
        self.grade1 = 0
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.final_exam = 0
        self.__final_grade = 0

    @property
    def final_grade(self):
        return self.__final_grade

    @final_grade.setter
    def final_grade(self, new_final_grade):
        self.__final_grade = new_final_grade

    def calc_grade(self):
        self.__final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam)/5


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
