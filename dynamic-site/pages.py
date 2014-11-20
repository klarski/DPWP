class Page(object):
    def __init__(self):
        self.head = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Handsome Hipster Coffee Roasters<title>
        </head>
        <body>
        '''
        self.body = '''
        <div>
            <img src=""/>
            <ul>
                <li>Home<li>
                <li>About</li>
                <li>Store</li>
            </ul>
        </div>

        <div id="coffee-bags">
            <div class="product">
                <img src="" />
            </div>

            <div class="product">
                <img src="" />
            </div>

            <div class="product">
                <img src="" />
            </div>

            <div class="product">
                <img src="" />
            </div>

            <div class="product">
                <img src="" />
            </div>

            <div class="product">
                <img src="" />
            </div>
        </div>

        '''
        self.close = '''
        </body>
        </html>
        '''