# this script will take care of the issue that all urls need to work if the user visists them
# the main.py script will run the web app

# we just need to run this script to run all the url's simulteaounasly

import justpy as jp

from about import AboutPage
from home import HomePage
from dictionary import DictionaryPage

# this will run the different pages
if __name__ == '__main__':
    jp.Route(AboutPage.path,AboutPage.serve)
    jp.Route(HomePage.path,HomePage.serve)
    jp.Route(DictionaryPage.path,DictionaryPage.serve)

# this will run the web app on the port

    jp.justpy(port=8001)

