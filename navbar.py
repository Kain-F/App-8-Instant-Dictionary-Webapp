import justpy as jp


class DefaultLayout(jp.QLayout):

    def __init__(self,view="hHh lpR fFf",**kwargs):
        super().__init__(view=view,**kwargs)

        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=self, show_if_above=True, dense='True', v_model='leftDrawerOpen',
                            side='left', border=True)

        # now we will populate our drawer with the links to the other pages
        # you can do this by using jp.A()

        scroll_area = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroll_area)
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
        jp.A(a=qlist, text='Home', href='/home', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='Dictionary', href='/dictionary', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='About', href='/about', classes=a_classes)
        jp.Br(a=qlist)

        button = jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon='menu', bordered=True,
                drawer=drawer)
        button.on('click',self.move_drawer)
        jp.QToolbar(a=toolbar, text='Instant dictionary')

    @staticmethod
    def move_drawer(widget,msg):
        print(widget.drawer.value)
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True


