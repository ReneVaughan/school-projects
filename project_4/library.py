'''
Name: Rene Vaughan
Class: Design Patterns for Web Programming
Assignment: Reusable Library
Date: 2/19/2015
'''

'''
Data Object Class-----------
The following is the data object class that is storing the information that the user input.
'''
class WorkoutData(object):
    def __init__(self):
        self.__workout = ''
        self.__weight = 0
        self.__minutes = 0
        self.__intensity = ''

    #Getter for workout
    @property
    def workout(self):
        return self.__workout

    #setter for workout - set's workout to strength by default if nothing is chosen
    @workout.setter
    def workout(self, wo):
        if wo == "":
            self.__workout = "Strength"
        else:
            self.__workout = wo

    #Getter for weight
    @property
    def weight(self):
        return self.__weight

    #Setter for weight - sets weight to 100 if a weight less than 99 is entered
    @weight.setter
    def weight(self, w):
        if w == "" or w < 99:
            self.__weight = 100
        #if int(w) < 99:
        #    self.__weight = 100
        else:
            self.__weight = w

    #Getter for minutes
    @property
    def minutes(self):
        return self.__minutes

    #Setter for minutes - sets minutes to 0 if nothing is entered
    @minutes.setter
    def minutes(self, m):
        if m == "":
            self.__minutes = 0
        else:
            self.__minutes = m

    #Getter for intensity
    @property
    def intensity(self):
        return self.__intensity

    #Setter for intensity - sets intensity to Low by default if nothing else is chosen
    @intensity.setter
    def intensity(self, it):
        if it == "":
            self.__intensity = "Low"
        else:
            self.__intensity = it





'''
Utilities Class--------------
The following class is the utilities class that will have the functions and calculations for the results view. View #2
'''
class WorkoutInformation(object):
    def __init__(self): #Initializer function
        self.work = WorkoutData()

    #This compiles the the information once the user submits the information - View #2
    def compile_list(self):
        output = ""
        output += "<div class='work'><h2><center>Workout Information:</center></h2> <center>Workout: " + self.work.workout + "</center><br/><center>Weight: " + str(self.work.weight) + "</center><br/><center>Minutes: " + str(self.work.minutes) + "</center><br/><center>Intensity: " + self.work.intensity + "</center></div>"
        return output

    #function to calculate the total calories burned
    def calculate_calories(self):
        minutes = self.work.minutes
        calories = .50
        total = int(minutes) * calories

        print total
        return "<div class='work'><center>Calories Burned:  " + str(total) + "!!</center></div>"

