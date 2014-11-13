class FormPage(object):
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
        self.body = '''
<h1>KimpMail</h1>
<h3>Create your KimpMail Account</h3>
<form>
    <ul>
        <li>
            <label>First Name:</label>
            <input class="text" type="text" name="fname"/>
        </li>

        <li>
            <label>Last Name: </label>
            <input class="text" type="text" name="lname"/>
        </li>

        <li>
            <label>Date of Birth:</label>
            <input class="date" type="date" name="dob">
        </li>

        <li>
            <label>Username:</label>
            <input class="text" type="text" name="username"><p>@kimpmail.com</p>
        </li>

        <li>
            <label>Password:</label>
            <input class="text" type="password" name="password">
        </li>

        <li>
            <label>Verify Password:</label>
             <input class="text" type="password" name="verify-password">
       </li>

        <li>
            <label>Prove that you are not a Robot:</label>
            <input class="text" type="password" name="verify-password">
       </li>

        <li>
            <button class="submit" type="submit" value="Submit" />Sign me up!</button>
        </li>
    </ul>

</form>


        '''
        self.__close = """
        </body>
    </html>
        """
    def print_out(self):
        all = self.head + self.body + self.__close
        return all


class ResultsPage(object):
    def __init__(self):
        pass