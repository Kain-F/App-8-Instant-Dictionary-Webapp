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
    #we will add some components to the webpage
    #to style our components we use the classes parameter and more information can be found on tailwindcss
    #in order to get the general background styling we need to put the components inside the div that defines the background

    jp.Input(a=div,placeholder = 'Enter first value',classes = 'form-input')
    jp.Input(a=div,placeholder = 'Enter second value',classes = 'form-input')
    jp.Div(a=div,text='Result goes here...')
    jp.Button(a=div,text = 'Calculate',
              # now we will make a border around our button
              classes = 'border border-blue-500 m-2 py-1 px-4 rounded text-blue-600 '
                        'hover:bg-red-500 hover:text-white')


    return wp



jp.justpy()