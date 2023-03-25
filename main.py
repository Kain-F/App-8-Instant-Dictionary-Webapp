# this script will take care of the issue that all urls need to work if the user visists them
# the main.py script will run the web app

# we just need to run this script to run all the url's simulteaounasly

import justpy as jp

from about import About
from home import HomePage

# this will run the different pages
jp.Route(About.path,About.serve)
jp.Route(HomePage.path,HomePage.serve)

# this will run the web app on the port
if __name__ == '__main__':
    jp.justpy(port=8001)

