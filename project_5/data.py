'''
Name: Rene Vaughan
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
Date: 2/26/2015
'''
'''
This is the main DataObject - It is setting up the attributes for: name of planet, distance from sun, number of moons,
length of year in Earth days, and fun facts. It's being called in Data class.
It's imported in page.py
'''
class Planet(object):
    def __init__(self):
        self.name = '' #name of planet
        self.dfs = '' #distance from sun
        self.moon = 0 #number of moons
        self.loy = '' #length of a year in Earth days
        self.fun_fact = '' #fun fact

'''
This is class is holding "Planet" data. It is storing the name, distance from the sun, number of moons, length of year
and fun facts about the planet.
It's imported in main.py
'''
class Data(object):
    def __init__(self):
        #data for planet Mercury
        mercury = Planet() #calling instance of planet
        mercury.name = "Mercury" #Planet Name
        mercury.dfs = "35,983,095 miles" #Distance from the sun
        mercury.moon = 0 #Number of moons
        mercury.loy = "88 days" #Lenth of Year in Earth Days
        #Some fun facts about the planet
        mercury.fun_fact = "Mercury is the closest planet to the sun. It orbits the sun so fast that the length of Mercury's day is equal to almost 59 Earth days!"

        #data for planet Venus
        venus = Planet() #calling instance of planet
        venus.name = "Venus" #Planet Name
        venus.dfs = "67,237,910 miles" #Distance from the sun
        venus.moon = 0 #Number of moons
        venus.loy = "225 days" #Lenth of Year in Earth Days
        #Some fun facts about the planet
        venus.fun_fact = "Venus is knowns as Earth's sister planet. It is similar in size, mass, density and composition. It can be observed once every century passing in front of the sun."

        #data for planet Earth
        earth = Planet() #calling instance of planet
        earth.name = "Earth" #Planet Name
        earth.dfs = "92,955,820 miles" #Distance from the sun
        earth.moon = 1 #Number of moons
        earth.loy = "365 days" #Lenth of Year in Earth Days
        #Some fun facts about the planet
        earth.fun_fact = "Earth is the 3rd planet from the sun. It's the 5th largest planet in our solar system. It's also the only known planet to harbor life."

        #data for planet Mars
        mars = Planet() #calling instance of planet
        mars.name = "Mars" #Planet Name
        mars.dfs = "141,633,260 miles" #Distance from the sun
        mars.moon = 2 #Number of moons
        mars.loy = "687 days" #Lenth of Year in Earth Days
        #Some fun facts about the planet
        mars.fun_fact = "Known as the Red Planet. Mars is thought to have once been like Earth. There are currently many studies being done to understand the history of Mars so we might have a better understanding of it's evolution. That understanding could lead to understanding the evolution of all planets including our own!"

        #data for planet Jupiter
        jupiter = Planet() #calling instance of planet
        jupiter.name = "Jupiter" #Planet Name
        jupiter.dfs = "483,682,810 miles" #Distance from the sun
        jupiter.moon = 63 #Number of moons
        jupiter.loy = "4,331 days" #Lenth of Year in Earth Days
        #Some fun facts about the planet
        jupiter.fun_fact = "Known as the Giant. Jupiter is the most massive planet in our solar system. It resembles a star in composition. Jupiter has a giant spinning storm called the Great Red Spot that has been observed for more than 300 years."

        #data for planet Saturn
        saturn = Planet() #calling instance of planet
        saturn.name = "Saturn" #Planet Name
        saturn.dfs = "885,904,700 miles" #Distance from the sun
        saturn.moon = 52 #Number of moons
        saturn.loy = "10,759 days" #Lenth of Year in Earth Days
        #Some fun facts about the planet
        saturn.fun_fact = "Known as the Ringed Planet. Saturn's ring system is the most extensive and complex in the solar system. It's rings extend hundreds of thousands of kilometers from the planet."

        #data for planet Uranus
        uranus = Planet() #calling instance of planet
        uranus.name = "Uranus" #Planet Name
        uranus.dfs = "1,783,939,400 miles" #Distance from the sun
        uranus.moon = 27 #Number of moons
        uranus.loy = "30,687 days" #Lenth of Year in Earth Days
        #Some fun facts about the planet
        uranus.fun_fact = "Known as the Blue Planet. Uranus is the 7th planet from the sun. It takes 84 years to complete one orbit around the sun! It's axis is almost horizontal. Many of it's moons are named after characters from the works of William Shakespeare."

        #data for planet Neptune
        neptune = Planet() #calling instance of planet
        neptune.name = "Neptune" #Planet Name
        neptune.dfs = "2,795,084,800 miles" #Distance from the sun
        neptune.moon = 13 #Number of moons
        neptune.loy = "60,190 days" #Lenth of Year in Earth Days
        #Some fun facts about the planet
        neptune.fun_fact = "Neptune is the 8th planet from the sun. It was the first planet located through mathematical predictions rather than through regular observations of the sky. The winds on Neptune are three times stronger than Jupiter's and and nine times stronger than Earth's. "

        #Array to store the planets/data - will be passed into mainHandler in main.py
        self.planet_list = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]





