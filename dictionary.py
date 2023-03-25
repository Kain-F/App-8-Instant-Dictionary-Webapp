import justpy as jp
import util

class DictionaryPage():
    path = '/dictionary'

    # by making serve a class method we will be able to get self as a dictionary instance
    # this will enable us to implement our functionality of showing the dictionary value of a word
    @classmethod
    def serve(cls,req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-blue-100 h-screen')
        div1 = jp.Div(a=div,classes = 'gap-2 p-4 border border-black')
        div2 = jp.Div(a=div,classes = 'grid grid-cols-2 gap-2 p-4 border border-black')
        div3 = jp.Div(a=div,classes = 'gap-2 p-4 border border-black')

        jp.Div(a=div1,text= 'Instant English dictionary', classes = 'text-4xl m-2 p-4')
        jp.Div(a=div1,text= 'Get the definition of any English word instantly as you type', classes = 'text-lg m-2')

        in_1 = jp.Input(a=div2,placeholder = 'Type in a word here',
                 classes = 'm-2 bg-amber-200 border-2 border-gray-200 rounded w-64 '
                           'focus:outline-none focus:border-purple-500 focus:bg-white '
                           'py-2 px-4')
        d_output = jp.Div(a=div3,
                          classes = 'm-2 p-2 text:lg '
                                    'border border-2 border-black h-40')
        jp.Button(a=div2, text='test it!', click=cls.result,
                  in1=in_1, d=d_output,
                  # now we will make a border around our button
                  classes='border border-blue-500 m-2 py-1 px-4 rounded text-blue-600 '
                          'hover:bg-red-500 hover:text-white')




        print(cls,req)
        return wp

    @classmethod
    def result(cls,widget,msg):
        print(widget.in1.value)

