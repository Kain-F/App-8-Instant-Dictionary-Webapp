import justpy as jp

class DictionaryPage():
    path = '/dictionary'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-blue-100 h-screen')
        jp.Div(a=div,text= 'This is the dictionary page', classes = 'text-4xl m-2')
        return wp
