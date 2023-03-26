import justpy as jp
import navbar
import page
from page import Page

class HomePage(page.Page):
    path= '/home'

    @classmethod
    def serve(cls,req):

        wp = jp.QuasarPage(tailwind=True)

        layout = navbar.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container,classes = 'bg-blue-100 h-screen')
        jp.Div(a=div, text='This is the home page', classes='text-4xl p-2')

        print(cls,req)
        return wp
