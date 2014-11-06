class Form(object):
    def __init__(self):
        self.head = """
        <!DOCTYPE HTML>
        <html>
            <head>
                <title>Voter's Registration Form</title>
            </head>
            <body>
        """
        self.body = """
            <h1>Voters Registration form</h1>
            <form>
                <ul>
                    <li>
                        <label>First Name:</label>
                        <input/>
                    </li>

                    <li>
                        <label>Last Name: </label>
                        <input/>
                    </li>

                    <li>
                        <label>Date of Birth:</label>
                        <input/>
                    </li>

                    <li>
                        <label>Address:</label>
                        <input>
                    </li>

                    <li>
                        <label>City:</label>
                        <input>
                    </li>

                    <li>
                        <label>State:</label>
                        <input>
                    </li>

                    <li>
                        <label>Zip Code:</label>
                        <input>
                    </li>

                    <li>
                        <label>ID Number:</label>
                        <input>
                    </li>

                    <li>
                        <label>Choice of Party:</label>
                        <input>
                    </li>

                    <li>
                        <label>Will you be 18 years old before or on election day?</label>
                        <input>
                    </li>
                <ul>
            </form>

        """
        self.close = """
            </body>
        </html>
        """