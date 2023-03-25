import justpy as jp

@jp.SetRoute('/home')
def first_page():
    """
    This function creates the webpage, for more information on styles and components
    go to tailwindcss.com
    """
    # we create an empty webpage
    wp = jp.WebPage()
    # to style our webpage we first make a main div and use the classes parameter and more information can be found on tailwindcss
    div = jp.Div(a=wp,classes = 'bg-blue-100 h-screen')

    # in order to put our components next to each other we will make a grid for them
    # each grid will be a div

    div1 = jp.Div(a=div, classes = 'grid grid-cols-3 gap-2 p-4 border border-black')

    #we will add some components to the webpage
    #to style our components we use the classes parameter and more information can be found on tailwindcss
    #in order to get the general background styling we need to put the components inside the div that defines the background

    in_1= jp.Input(a=div1,placeholder = 'Enter first value',classes = 'form-input')
    in_2= jp.Input(a=div1,placeholder = 'Enter second value',classes = 'form-input')
    d_output =jp.Div(a=div1,text='Result goes here...')


    # in order to put our components next to each other we will make a grid for them
    # each grid will be a div

    div2 = jp.Div(a=div, classes='grid grid-cols-2 gap-4 p-4 border border-black')

    jp.Button(a=div2,text = 'Calculate',click = sum_up,
              in1 = in_1, in2 = in_2, d = d_output,
              # now we will make a border around our button
              classes = 'border border-blue-500 m-2 py-1 px-4 rounded text-blue-600 '
                        'hover:bg-red-500 hover:text-white')
    jp.Div(a=div2, text = 'I am div')

    return wp

# in order to execute the code on the click event we need to add widget and msg params in the function
def sum_up(widget,msg):
    input1 = widget.in1.value
    input2 = widget.in2.value
    result = float(input1) + float(input2)
    widget.d.text = result







jp.justpy()