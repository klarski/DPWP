class FormPage(object):
    def __init__(self):
        self.title = "Welcome"
        self.css = ""
        self.head = """
    <!DOCTYPE HTML>
    <html>
        <head>
            <title>{self.title}</title>
            <link href="css/main.css" rel="stylesheet" type="text/css" />
            <link href='http://fonts.googleapis.com/css?family=Josefin+Sans:600' rel='stylesheet' type='text/css'>
        </head>
        <body>
        """
        self.body = '''
<img src="images/kimpmail.png" alt="KimpMail" width="400"/>
<div id="header">
    <ul>
        <li>LOGIN</li>
        <li>ABOUT</li>
    </ul>
</div>

<h3>Create your KimpMail Account:</h3>
<div id="form">
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
                <input class="text" type="text" name="username"><span>@kimpmail.com</span>
            </li>

            <li>
                <label>Password:</label>
                <input class="text" type="password" name="password">
            </li>

            <li>
                <label>Verify Password:</label>
                 <input class="text" type="password" name="verify-password">
           </li>

            <li id="robot">
                <label>Prove that you are not a Robot:</label><span><img src=images/robot.jpg width="100" /></span>
                <input class="text" type="number" name="robot">
           </li>

            <li>
                <button class="submit" type="submit" value="Submit" />Sign me up!</button>
            </li>
        </ul>
    </form>
<div>
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