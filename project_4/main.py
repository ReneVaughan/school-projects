'''
Name: Rene Vaughan
Class: Design Patterns for Web Programming
Assignment: Reusable Library
Date: 2/19/2015
'''

import webapp2
from pages import WorkoutForm #importing the WorkoutForm class from pages.py
from library import WorkoutData, WorkoutInformation #importing the DatabObject (WorkoutData) and the Utilities Class (WorkoutInformation)

class MainHandler(webapp2.RequestHandler):
    def get(self):

        wf = WorkoutForm() #pages object

        wd = WorkoutData() #data object

        wi = WorkoutInformation() #results object

        '''
        This is collecting the data from the form as well as using the functions in the utility class.
        If the submit button is hit then it will print the compile list otherwise just the form_view will print.
        '''
        if self.request.GET:
            wd.workout = self.request.GET['workout']
            wd.weight = self.request.GET['weight']
            wd.minutes = self.request.GET['minutes']
            wd.intensity = self.request.GET['intensity']

            wi.work = wd

            #calling the functions from the utilities class - compile_list and calculate_calories which calculates calories burned
            wf.body = wi.compile_list() + wi.calculate_calories()

            self.response.write(wf.form_view())

        else:
            self.response.write(wf.form_view())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
