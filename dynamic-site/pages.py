class Page(object):
    def __init__(self):
        self.head = '''<!DOCTYPE HTML>
        <html>
        <head>
            <title>Handsome Hipster Coffee Roasters</title>
            <link href="css/main.css" rel="stylesheet" type="text/css" />
            <link href='http://fonts.googleapis.com/css?family=Lato:300,400,700' rel='stylesheet' type='text/css'>
        </head>
        <body>
        '''
        self.header = '''
        <div id="header">
            <img src="images/hhc.png" alt="logo" width="300"/>
            <ul>
                <li>Home</li>
                <li>About</li>
                <li>Store</li>
            </ul>
        </div>
        '''
        self.body = ""
        self.close = '''
        </body>
        </html>
        '''

    def print_out(self):
        return self.head + self.header + self.body + self.close

class ContentPage(Page):
    def __init__(self):
        Page.__init__(self)
        self.product_view = '''
        <div id="feat-product">
            <img src="http://placehold.it/350x350" width="350"/>
                <div class="feat-info">
                    <h3>{name}</h3><span>{price}</span>
                    <p>Roast: {roast}</p>
                    <p>Regions: {regions}</p>
                    <p>Flavors: {flavors}</p>
                </div>
        </div>
        '''
        self.body = '''
        <div id="coffee-bags">
            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><span>{price}</span>
            </div>

            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><span>{price}</span>
            </div>

            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><span>{price}</span>
            </div>

            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><span>{price}</span>
            </div>

            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><span>{price}</span>
            </div>

            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><span>{price}</span>
            </div>
        </div>
        '''

    def print_out(self):
        return self.head + self.header + self.product_view + self.body + self.close
