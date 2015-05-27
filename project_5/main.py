'''
Name: Rene Vaughan
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
Date: 2/26/2015
'''
import webapp2
from page import ContentPage #importing ContentPage class from page.py file
from data import Data #importing Data class from data.py file


class MainHandler(webapp2.RequestHandler):
    def get(self):

        c = ContentPage()#instance for ContentPage
        planet = Data()#Instance for Data for planets

        '''
        This conditional is getting the link information from planet_links in the class Content Page.
        It's saying to look at the key for each link and display the appropriate planet information from the
        array planet_list in the Data class in data.py file.
        '''
        if self.request.GET:
            link = self.request.GET['planet']
            if link == "mercury":
                c.planet_info_out(planet.planet_list[0])#This is passing Mercury information
            elif link == "venus":
                c.planet_info_out(planet.planet_list[1])#This is passing Venus information
            elif link == "earth":
                c.planet_info_out(planet.planet_list[2])#This is passing Earth information
            elif link == "mars":
                c.planet_info_out(planet.planet_list[3])#This is passing Mars information
            elif link == "jupiter":
                c.planet_info_out(planet.planet_list[4])#This is passing Jupiter information
            elif link == "saturn":
                c.planet_info_out(planet.planet_list[5])#This is passing Saturn information
            elif link == "uranus":
                c.planet_info_out(planet.planet_list[6])#This is passing Uranus information
            elif link == "neptune":
                c.planet_info_out(planet.planet_list[7])#This is passing Neptune information

            self.response.write(c.print_page()) #Prints print_page from page.py

        else:
            self.response.write(c.print_page()) #Prints print_page from page.py - no planet_info will print if there is no active link


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
