class FormPage(object):
    def __init__(self):
        # this is the header for the form page
        self.head = """
    <!DOCTYPE HTML>
    <html>
        <head>
            <title>KimpMail.com</title>
            <link href="css/main.css" rel="stylesheet" type="text/css" />
            <link href='http://fonts.googleapis.com/css?family=Josefin+Sans:600' rel='stylesheet' type='text/css'>
        </head>
        <body>
        """
        # this is the body html for the form and inputs
        self.body = '''
<img src="images/kimpmail.png" alt="KimpMail" width="400"/>
<div id="header">
    <ul>
        <li>LOGIN</li>
        <li>ABOUT</li>
    </ul>
</div>

<h2>Create your KimpMail Account:</h2>
<div id="form" method="GET">
    <form>
        <ul>
            <li>
                <label>First Name:</label>
                <input class="text" type="text" name="fname" required/>
            </li>

            <li>
                <label>Last Name: </label>
                <input class="text" type="text" name="lname" required/>
            </li>

            <li>
                <label>Date of Birth:</label>
                <input class="date" type="date" name="dob" required>
            </li>

            <li>
                <label>Username:</label>
                <input class="text" type="text" name="username" required><span>@kimpmail.com</span>
            </li>

            <li>
                <label>Password:</label>
                <input class="text" type="password" name="password" required>
            </li>

            <li>
                <label>Verify Password:</label>
                 <input class="text" type="password" name="verify-password" required>
           </li>

            <li id="robot">
                <label>Prove that you are not a Robot:<span><img src=images/robot.jpg width="100" /></span></label>
                <input class="text" type="number" name="robot" required>
           </li>

            <li>
                <button id="form-btn" class="submit" type="submit" value="Submit" />Sign me up!</button>
            </li>
        </ul>
    </form>
<div>
        '''
        # this is the closing html for the form page
        self.__close = """
        </body>
    </html>
        """
        # this method returns all the html to be written to the page
    def print_out(self):
        all = self.head + self.body + self.__close
        return all


class ResultsPage(object):
    def __init__(self):
        # this is the header html for the results page
        self.head = """
    <!DOCTYPE HTML>
    <html>
        <head>
            <title>KimpMail.com</title>
            <link href="css/main.css" rel="stylesheet" type="text/css" />
            <link href='http://fonts.googleapis.com/css?family=Josefin+Sans:600' rel='stylesheet' type='text/css'>
        </head>
        <body>
        """
         # this is the body html for the results page
        self.body = '''
<img src="images/kimpmail.png" alt="KimpMail" width="400"/>
<div id="header">
    <ul>
        <li>LOGIN</li>
        <li>ABOUT</li>
    </ul>
</div>
    <h2>Verify your information:</h2>
        <div id="form-data">
            <ul>
                <li>First Name: {data.fname}</li>
                <li>Last Name: {data.lname}</li>
                <li>Date of Birth: {data.dob}</li>
                <li>Username: {data.username}</li>
                <li>Password: {data.password}</li>
            </ul>
            <button class="submit">Edit Information</button>
            <button class="submit">Submit</button>
    </div>
        '''
         # this is the closing html for the results page
        self.close = """
        </body>
    </html>
        """