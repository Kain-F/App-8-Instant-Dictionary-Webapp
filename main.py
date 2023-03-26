# this script will take care of the issue that all urls need to work if the user visists them
# the main.py script will run the web app

# we just need to run this script to run all the url's simulteaounasly
import inspect
import justpy as jp

import page
from page import Page

from about import AboutPage
from home import HomePage
from dictionary import DictionaryPage

imports = list(globals().values())

# this will run the different pages
if __name__ == '__main__':
    #we can iterate over the dictionary of imports
    for obj in imports:
        if inspect.isclass(obj):
            if issubclass(obj,page.Page) and obj is not page.Page:
                print(obj)
                jp.Route(obj.path,obj.serve)

# this will run the web app on the port

    jp.justpy(port=8001)

