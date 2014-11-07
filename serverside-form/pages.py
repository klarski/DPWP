class Form(object):
    def __init__(self):
        self.head = """
        <!DOCTYPE HTML>
        <html>
            <head>
                <title>Voter's Registration Form</title>
                <link href='http://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
                <link href="css/main.css" rel="stylesheet" type="text/css" />
            </head>
            <body>
            <div class="header">
                <img src="images/poll-img.png" width="100" height="100" />
                <h1>Voters Registration form</h1>
            </div>
        """
        self.body = """
            <div id="criteria">
                <h3>To register to vote you must:</h3>
                    <p> Be a citizen of the United States, be a legal resident of the county, be at least 17 1/2 years of age to register and 18 years of age to vote, Nnt be serving a sentence for conviction of a felony involving moral turpitude, and Hhve not been found mentally incompetent by a judge</p>

            </div>
            <div id="form">
                <form method="GET">
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
                            <label>Address:</label>
                            <input class="text" type="text" name="address">
                        </li>

                        <li>
                            <label>City:</label>
                            <input class="text" type="text" name="city">
                        </li>
                        <li>
                            <label>State:</label>
                            <select name="state">
                                <option value="AL">AL</option>
                                <option value="AK">AK</option>
                                <option value="AZ">AZ</option>
                                <option value="AR">AR</option>
                                <option value="CA">CA</option>
                                <option value="CO">CO</option>
                                <option value="CT">CT</option>
                                <option value="DE">DE</option>
                                <option value="DC">DC</option>
                                <option value="FL">FL</option>
                                <option value="GA">GA</option>
                                <option value="HI">HI</option>
                                <option value="ID">ID</option>
                                <option value="IL">IL</option>
                                <option value="IN">IN</option>
                                <option value="IA">IA</option>
                                <option value="KS">KS</option>
                                <option value="KY">KY</option>
                                <option value="LA">LA</option>
                                <option value="ME">ME</option>
                                <option value="MD">MD</option>
                                <option value="MA">MA</option>
                                <option value="MI">MI</option>
                                <option value="MN">MN</option>
                                <option value="MS">MS</option>
                                <option value="MO">MO</option>
                                <option value="MT">MT</option>
                                <option value="NE">NE</option>
                                <option value="NV">NV</option>
                                <option value="NH">NH</option>
                                <option value="NJ">NJ</option>
                                <option value="NM">NM</option>
                                <option value="NY">NY</option>
                                <option value="NC">NC</option>
                                <option value="ND">ND</option>
                                <option value="OH">OH</option>
                                <option value="OK">OK</option>
                                <option value="OR">OR</option>
                                <option value="PA">PA</option>
                                <option value="RI">RI</option>
                                <option value="SC">SC</option>
                                <option value="SD">SD</option>
                                <option value="TN">TN</option>
                                <option value="TX">TX</option>
                                <option value="UT">UT</option>
                                <option value="VT">VT</option>
                                <option value="VA">VA</option>
                                <option value="WA">WA</option>
                                <option value="WV">WV</option>
                                <option value="WI">WI</option>
                                <option value="WY">WY</option>
                            </select>

                        </li>

                        <li>
                            <label>Zip Code:</label>
                            <input class="text" type="text" name="zip"  pattern="\d*">
                        </li>

                        <li>
                            <label>ID Number:</label>
                            <input class="text" type="text" name="idnum">
                        </li>

                        <li>
                            <label>Choice of Party:</label>
                                <select name="party">
                                    <option value="Democrat">Democrat</option>
                                    <option value="Republican">Republican</option>
                                    <option value="Independent">Independent</option>
                                    <option value="Other">Other</option>
                                </select></br>
                        </li>

                        <li>
                            <p>Will you be 18 years old before or on election day?</p>
                            <div id="radio-answers">
                                <input class="age" type="radio" name="age" value="Yes">Yes
                                <input class="age" type="radio" name="age" value="No">No
                            </div>
                        </li>

                        <li>
                            <button class="submit" type="submit" value="Submit" />Register</button>
                        </li>
                    <ul>
                </form>
            </div>

        """
        self.body_page2 = """
            <div id="answers">
            <h2>{age}</h2>
                <ul>
                    <li>First Name: {fname}</li>
                    <li>Last Name: {lname}</li>
                    <li>Date of Birth: {dob}</li>
                    <li>Address: {address}, {city}, {state}, {zip}</li>
                    <li>ID number: {idnum}</li>
                    <li>Party: {party}<li>
                </ul>
            <div>

        """
        self.close = """
            <div class="footer>
                <p>This form was created by Kristen Kozinski</p>
            </div>
            </body>
        </html>
        """