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
        self.product_view = '''
        <div>

        </div>
        '''
        self.body = '''
        <div id="coffee-bags">
            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><p>{price}</p>
                <p>Roast: {roast}</p>
                <p>Regions: {regions}</p>
                <p>Flavors: {flavors}</p>
            </div>

            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><p>{price}</p>
                <p>Roast: {roast}</p>
                <p>Regions: {regions}</p>
                <p>Flavors: {flavors}</p>
            </div>

            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><p>{price}</p>
                <p>Roast: {roast}</p>
                <p>Regions: {regions}</p>
                <p>Flavors: {flavors}</p>
            </div>

            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><p>{price}</p>
                <p>Roast: {roast}</p>
                <p>Regions: {regions}</p>
                <p>Flavors: {flavors}</p>
            </div>

            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><p>{price}</p>
                <p>Roast: {roast}</p>
                <p>Regions: {regions}</p>
                <p>Flavors: {flavors}</p>
            </div>

            <div class="product">
                <img src="http://placehold.it/200x200" width="200"/>
                <h3>{name}</h3><p>{price}</p>
                <p>Roast: {roast}</p>
                <p>Regions: {regions}</p>
                <p>Flavors: {flavors}</p>
            </div>
        </div>

        '''
        self.close = '''
        </body>
        </html>
        '''

    def print_out(self):
        all = self.head + self.header + self.product_view + self.body + self.close
        return all