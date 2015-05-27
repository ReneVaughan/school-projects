'''
Name: Rene Vaughan
Class: Design Patterns for Web Programming
Assignment: Reusable Library
Date: 2/19/2015
'''

'''
This is the WorkoutForm class - it holds the HTML for how the form view looks for requesting information from the user.
There are 3 different attributes that
'''

class WorkoutForm(object): #View 1 of the actual Form
    def __init__(self):
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>My Workouts!</title>
        <link href='http://fonts.googleapis.com/css?family=Roboto:300' rel='stylesheet' type='text/css'>
        <link href="css/style.css" type="text/css" rel="stylesheet" />

    </head>

    <body>

        """

        '''
        The following code is the html for the My Workout Form. It will ask the user for a few things.
        The first will be the type of workout with a selction. The next is the users weight.
        Then the length of the workout in minutes. Then it will ask for the intensity.
        It will ask this information for 1 workouts because it's assuming the user's account is set up with a goal of 1 workouts per week.


        '''

        self.body = """

        <div id="container">
            <h2><center>My Workouts This Week!</center></h2>
            <h4><center>Your account is currently set up with a goal of 1 workout per week. You can adjust this at any time.</center></h4>
            <form id="myworkout" method="GET" action="">
                <legend><center>Workout #1</center></legend>
                    <label>Workout Type:</label>
                        <select name="workout" required>
                            <option value="Strength">Strength</option>
                            <option value="Endurance">Endurance</option>
                            <option value="Flexibility">Flexibility</option>
                        </select>
                        </br>


                    <label>Weight:</label>
                        <input id="weight" type="text" name="weight" required>
                        </br>


                    <label>Length of Workout(minutes):</label>
                        <input id="minutes" type="text" name="minutes" required>
                        </br>


                    <label>Intensity:</label>
                        <select name="intensity" required>
                            <option value="Low">Low</option>
                            <option value="Medium">Medium</option>
                            <option value="High">High</option>
                        </select>

                        </br>
                        </br>

                    <input id="button" type="submit" value="Submit" onsubmit="validateFunction()" />

            </form>
        </div>

        """

        #This is the closeing section of the html
        self.close = """
        <script src="js/validate.js" type="text/javascript"></script>
    </body>
</html>

        """


    '''
    This method/function is the print out for the form view. View #1
    '''
    def form_view(self):
        all = self.head + self.body + self.close
        return all

