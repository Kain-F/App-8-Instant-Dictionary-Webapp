import justpy as jp

class DictionaryPage():
    path = '/dictionary'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-blue-100 h-screen')

        jp.Div(a=div,text= 'Instant English dictionary', classes = 'text-4xl m-2 p-4')
        jp.Div(a=div,text= 'Get the definition of any English word instantly as you type', classes = 'text-lg m-2')

        jp.Input(a=div,placeholder = 'Type in a word here',
                 classes = 'm-2 bg-amber-200 border-2 border-gray-200 rounded w-64 '
                           'focus:outline-none focus:border-purple-500 focus:bg-white '
                           'py-2 px-4')
        jp.Div(a=div,classes = 'm-2 p-2 text:lg '
                               'border border-2 border-black h-40')
        return wp
