class Page(object):
    def __init__(self):
        self.title = "Welcome"
        self.css = ""
        self.head = """
    <!DOCTYPE HTML>
    <html>
        <head>
            <title>{self.title}</title>
        </head>
        <body>
        """
        self.body = ""
        self.__error = ""
        self.__close = """
        </body>
    </html>
        """

    def print_out(self):
        all = self.head + self.body + self.__error + self.__close
        return all