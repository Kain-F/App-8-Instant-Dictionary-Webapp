import justpy as jp

# every page will get its own class in their own file

class About():
    path = '/about'


    @classmethod
    def serve(cls,req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header,title='Instant dictionary')
        drawer = jp.QDrawer(a = layout,show_if_above = True, dense='True',v_model = 'leftDrawerOpen',
                            side = 'left', border = True)

        #now we will populate our drawer with the links to the other pages
        #you can do this by using jp.A()

        scroll_area= jp.QScrollArea(a=drawer,classes = 'fit')
        qlist= jp.QList(a=scroll_area)
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
        jp.A(a=qlist,text = 'Home', href = '/home', classes = a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist,text = 'Dictionary', href = '/dictionary',classes = a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist,text = 'About', href = '/about',classes = a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a = toolbar,dense=True,flat=True,round=True,icon='menu',bordered=True,
                 drawer=drawer,click = cls.move_drawer)
        jp.QToolbar(a=toolbar,text='Instant dictionary')

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes='bg-blue-100 h-screen')
        jp.Div(a=div,text= 'This is the about page', classes = 'text-4xl m-2')
        jp.Div(a=div,text= """        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at lobortis dui, quis tempus dui. Suspendisse lobortis lacus porta turpis semper, sit amet varius enim blandit. Nam rhoncus malesuada maximus. Vivamus non sapien ultricies, tempor elit nec, finibus metus. Duis dignissim libero justo, in suscipit neque placerat at. Curabitur convallis scelerisque turpis, eget convallis metus tincidunt vitae. Pellentesque porta tellus id nunc lacinia, nec pulvinar risus dictum. Integer vehicula elit sit amet lectus hendrerit, vitae rutrum nunc ullamcorper. Sed quis commodo quam, sed consectetur ante. Quisque tempus ipsum a ex rhoncus laoreet. Suspendisse finibus cursus condimentum. Suspendisse potenti. Duis non pulvinar mi. Quisque eget diam tristique, porttitor odio nec, pharetra augue.
        Sed at lacus vel turpis porta semper. Suspendisse luctus dolor eget risus iaculis, ut faucibus ligula tempor. Praesent et lectus sit amet ipsum sollicitudin accumsan. Vestibulum placerat lectus non ligula pharetra sodales. Phasellus felis urna, dapibus ut semper nec, ornare nec tortor. Quisque sollicitudin sapien lectus. Integer consequat arcu neque. Curabitur aliquet nec risus porttitor elementum. Fusce a augue egestas, porta orci viverra, vestibulum dui. Vestibulum nulla lorem, semper ac auctor id, venenatis in quam. In hac habitasse platea dictumst. Curabitur eu leo sed justo pulvinar vulputate eu id ligula. Sed ac ligula ut mi dapibus dapibus.
        Ut tempor, ex in hendrerit luctus, massa nunc scelerisque dui, at aliquam tellus purus sit amet ipsum. Donec ipsum ex, iaculis ut porta at, tristique id mauris. Maecenas eu augue quis risus vestibulum feugiat. Cras consequat, turpis a tempor dapibus, ipsum odio venenatis ante, id lacinia turpis quam sed nunc. Aliquam vulputate massa ac tristique laoreet. Suspendisse id varius ligula. Suspendisse non risus vel lacus egestas porta. Maecenas quis ullamcorper lectus. Nam luctus egestas vehicula. Suspendisse ac leo molestie, feugiat lectus aliquam, mattis turpis. Sed bibendum viverra urna, ut faucibus justo sodales ac. Cras ac tortor sed velit porttitor convallis vitae in augue. Aliquam eu lorem est. Donec sit amet lacus lacinia, varius purus at, efficitur nisl. Morbi rutrum fermentum purus, vel faucibus leo accumsan vel. Suspendisse ut ipsum a enim aliquam luctus.
        Donec vitae neque vitae ligula egestas tempor. Aliquam suscipit eu lorem ut placerat. Quisque elementum fringilla mauris, sit amet porta ligula lacinia vel. Donec varius, leo in tincidunt egestas, lectus neque rutrum nibh, sed dictum metus nulla a ipsum. Praesent lacinia lectus molestie nisi fermentum, vitae suscipit augue faucibus. Duis id eros lectus. Suspendisse in ultrices urna. Vestibulum placerat dui a lectus maximus ultrices. Duis sagittis nibh et ligula ultricies ornare. Aliquam erat volutpat. Etiam auctor nisl dui, id cursus ex tristique id.
        Praesent lobortis in nisi nec pretium. Aenean et leo ac ex accumsan tempus at in tellus. Donec nec facilisis ante. Nam vel fermentum ex, eget dapibus ipsum. Vivamus efficitur odio magna, ut sodales elit interdum sed. Mauris a ipsum non sem tincidunt tristique. Nunc vel purus suscipit, congue est id, finibus tellus. Cras at fermentum lorem.
        """, classes = 'text-lg ')
        print(cls,req)
        return wp

    @staticmethod
    def move_drawer(widget,msg):
        print(widget.drawer.value)
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True




