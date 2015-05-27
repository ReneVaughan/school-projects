'''
Name: Rene Vaughan
Class: Design Patterns for Web Programming
Assignment: Dynamic Site
Date: 2/26/2015
'''

from data import Planet #import Planet class from data.py

'''
This is a the main/superclass for ContentPage. It sets up head, body and closing HTML.
'''
class Page(object):
    def __init__(self):
        #attribute set up for head section - hold main css links and link to Google Font and Title
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Planet Fun Facts!</title>
        <link href='http://fonts.googleapis.com/css?family=Roboto:300' rel='stylesheet' type='text/css'>
        <link href="css/style.css" type="text/css" rel="stylesheet" />

    </head>

    <body>

        '''
        #attribute set up for body
        self.body = ''

        #attribute for close - closes off body and html tags
        self.close = '''
    </body>
</html>

        '''
    #print function for main html - is overriden by print_out function in ContentPage
    def print_page(self):
        return self.head + self.body + self.close

'''
ContentPage is a subclass to Page - it is creating more details. It's storing all the content.
It's setting up the planet links that are getting passed information of the planets from main.py.
The Planet Class that is imported is setting a placeholder for the information/actual data being passed in from main.py - that
data is coming crom data.py.
The links "planet_links" are going to determine which planet information is being displayed.
'''
class ContentPage(Page):
    def __init__(self):
        super(ContentPage, self).__init__()
        self.planet_info = '' #Set up of planet_info attribute - called in planet_info_out
        #content open attribute setting up opening div - id of content
        self.content_open = '<div id=content>'
        #main content/information for page
        self.main_content = """
        <h2>Planet Fun Facts!</h2>
        <section id ="intro">
            <h4><center>What is a planet?</center></h4>
                <p>What is a planet? Well, they are large, up in the sky and we can't really see them, but they look pretty in pictures. These things are true, but they are so much more than that and much cooler!
                    </br></br>Planets have been observed for many years and many early cultures considered them emissaries of deities. It was also thought that the Sun, planets and all other objects orbited around Earth.
                </p>
                <p>Our knowledge and understanding of planets have come a long way. We now have a better understanding of what planets are and how to classify them. How we define them today is by determining a few factors:</p>
                    <ul id="facts">
                        <li>It has to orbit a sun.</li>
                        <li>It needs sufficient mass to assume a nearly round shape.</li>
                        <li>It can't be a satellite (moon).</li>
                        <li>It has to have cleared the neighborhood around its orbit.</li>
                    </ul>
                <p>There are still many studies and professions dedicated to more research and discovery of other planets in outer space. New planets beyond our solar system are being discovered all the time!</p>
            <h4><center>Explore the planets in our Solar System!</center></h4>
        </section>
        """
        #links are set with images - they tie to main.py - active link determines which Planet info is passed - it prints in planet_info_out
        self.planet_links = """
        <div id="links">
            <ul>
                <li id="mercury" class="main">
                    <a href="?planet=mercury"><img src="images/mercury.jpg" alt="Mercury" style="width: 75px; height: 75px"></a>
                </li>
                <li id="venus" class="main">
                    <a href="?planet=venus"><img src="images/venus.jpg" alt="Venus" style="width: 75px; height: 75px"></a>
                </li>
                <li id="earth" class="main">
                    <a href="?planet=earth"><img src="images/earth.jpg" alt="Earth" style="width: 75px; height: 75px"></a>
                </li>
                <li id="mars" class="main">
                    <a href="?planet=mars"><img src="images/mars.jpg" alt="Mars" style="width: 75px; height: 75px"></a>
                </li>
                <li id="jupiter" class="main">
                    <a href="?planet=jupiter"><img src="images/jupiter.jpg" alt="Jupiter" style="width: 75px; height: 75px"></a>
                </li>
                <li id="saturn" class="main">
                    <a href="?planet=saturn"><img src="images/saturn.jpg" alt="Saturn" style="width: 75px; height: 75px"></a>
                </li>
                <li id="uranus" class="main">
                    <a href="?planet=uranus"><img src="images/uranus.jpg" alt="Uranus" style="width: 75px; height: 75px"></a>
                </li>
                <li id="neptune" class="main">
                    <a href="?planet=neptune"><img src="images/neptune.jpg" alt="Neptune" style="width: 75px; height: 75px"></a>
                </li>
            </ul>
        </div>
        """
        #footer
        self.footer = """
        <div id="footer">
            <h5><center>Student: Rene Vaughan</center></h5>
        </div>
        """
        #close attribute setup
        self.content_close = ""

    #This is setting the planet info so the actual data can be passed from main.py. What gets sent is determined by what link is active.
    def planet_info_out(self, pl):
        self.planet_info = '<div id="planets"><center> <b>Planet Name:</b> ' + pl.name + '</br> <b>Distance From the Sun:</b> ' + pl.dfs + '</br> <b>Number of Moons:</b> ' + str(pl.moon) + '</br> <b>Length of Year in Earth Days:</b> ' + pl.loy + '</br> <b>Fun Facts:</b> ' + pl.fun_fact + '</center></div>'
        #close attribute called - end of page - closing off div with id of content.
        self.content_close = '</div>'
    #This print_page overrides the one in Page - it is printing all the attributes set up in ContentPage. Only planet_info will show once a link is activated.
    def print_page(self):
        return self.head + self.body + self.content_open + self.main_content + self.planet_links + self.planet_info + self.footer + self.content_close + self.close
