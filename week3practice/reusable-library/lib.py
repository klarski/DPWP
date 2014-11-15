class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []

    def add_movie(self, m):
        self.__movie_list.append(m)
        print m.title

    def compile_list(self):
        output = ' '
        for movie in self.__movie_list:
            output += 'Title:' + movie.title + ' (' + str(movie.year) + ') ' + 'Directed by:' + movie.director + '</br>'
        return output


    def calc_time_span(self):
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)
        years.sort()
        num = len(years) - 1
        span = years[num] - years[0]
        return 'The spam between the films entered is ' + str(span)


class MovieData(object):  # create data object
    def __init__(self):
        self.title = ""
        self.__year = ""  # check for valid year
        self.director = ""

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if y > 2014:
            print "Error, Invalid date!"
            self.__year = 2014
        else:
            self.__year = y