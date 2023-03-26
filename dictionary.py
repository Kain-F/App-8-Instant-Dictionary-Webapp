import justpy as jp

import page
import util
import navbar
from page import Page

class DictionaryPage(page.Page):
    path = '/dictionary'

    # by making serve a class method we will be able to get self as a dictionary instance
    # this will enable us to implement our functionality of showing the dictionary value of a word
    @classmethod
    def serve(cls,req):
        wp = jp.QuasarPage(tailwind=True)

        layout = navbar.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=layout)

        # this is the general lay-out of the page we have 3 sections stuck in one big div
        div = jp.Div(a=container, classes='bg-blue-100 h-screen')
        div1 = jp.Div(a=div,classes = 'gap-2 p-4 border border-black')
        div2 = jp.Div(a=div,classes = 'grid grid-cols-2 gap-2 p-4 border border-black')
        div3 = jp.Div(a=div,classes = 'gap-2 p-4 border border-black')

        # div1
        # this is the header of the webpage and contains no functionality
        jp.Div(a=div1,text= 'Instant English dictionary', classes = 'text-4xl m-2 p-4')
        jp.Div(a=div1,text= 'Get the definition of any English word instantly as you type', classes = 'text-lg m-2')
        #div3
        # this section will show the result
        d_output = jp.Div(a=div3,
                          classes = 'm-2 p-2 text:lg '
                                    'border border-2 border-black h-40')
        # div2
        # this section will contain the input box and the button it will have the on-click event handler in the button
        in_1 = jp.Input(a=div2, placeholder='Type in a word here', outputdiv=d_output,
                        classes='m-2 bg-amber-200 border-2 border-gray-200 rounded w-64 '
                                'focus:outline-none focus:border-purple-500 focus:bg-white '
                                'py-2 px-4')
        in_1.on('input', cls.get_definition)

        print(cls,req)
        return wp

    @staticmethod
    # this is the on click event handler that gets the definition
    def get_definition(widget,msg):
        input = widget.value
        definition = util.Definition(term=input).get()
        # with the join method we transform our tuple into defintions underneath eachother
        widget.outputdiv.text = " ".join(definition)

