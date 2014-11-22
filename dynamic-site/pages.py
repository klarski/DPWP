class Page(object):
    def __init__(self):
        self.head = '''<!DOCTYPE HTML>
        <html>
        <head>
            <title>Handsome Hipster Coffee Roasters</title>
            <link href="css/main.css" rel="stylesheet" type="text/css" />
            <link href='http://fonts.googleapis.com/css?family=Lato:300,400,700' rel='stylesheet' type='text/css'>
            <link href='http://fonts.googleapis.com/css?family=Vast+Shadow' rel='stylesheet' type='text/css'>
        </head>
        <body>
        '''
        self.header = '''
        <div id="header">
            <img src="images/hhc.png" alt="logo" width="300"/>
            <ul>
                <li><a href="http://klarski.github.io/handsome-hipster/index.html" target=_blank >Home</a></li>
                <li><a href="http://klarski.github.io/handsome-hipster/index.html#about" target=_blank>About</a></li>
                <li>Cart</li>
            </ul>
        </div>
        '''
        self.main_product = ""
        self.all_the_coffee = ""
        self.close = '''
        <footer>
            <div class="image-credit">
                <h3>Image Credits</h3>
                    <ul>
                      <li><a href="https://flic.kr/p/97JMPT" target="_blank">Brooklyn Blend</a></br></li>
                      <li><a href="https://flic.kr/p/eppLDF" target="_blank">Portland Blend</a></br></li>
                      <li><a href="https://flic.kr/p/eeQ6RR" target="_blank">Austin Blend</a></br></li>
                      <li><a href="https://flic.kr/p/bW9MmR" target="_blank">Boston Blend</a></br></li>
                      <li><a href="https://flic.kr/p/9BbeEa" target="_blank">SanFran Blend</a></br></li>
                    <ul>
              </div>
        </footer>
        </body>
        </html>
        '''

    def print_out(self):
        return self.head + self.header + self.main_product + self.all_the_coffee + self.close

class ContentPage(Page):
    def __init__(self):
        Page.__init__(self)

    def product_view(self, main_p):
        self.main_product = '<div class="feat-product"><img src="' + main_p.image + '" width="300"/><h1>' + main_p.name + '</h2><h3>$' + str(main_p.price) + '</h3><p>Roast: ' + main_p.roast + '</br>Regions: ' + main_p.regions + '</br>Flavors: ' + main_p.flavors + '</p><button>Add to Cart</button></div>'


    def coffee_buttons(self, a):
        self.coffee_thumb_div = '<div id="coffee-bags"><h1>Coffee Blends</h1>'

        self.coffee_thumb1 = '<div class="product">' + '<a href="?name=' + a[0].name + '"><img src="images/thumb1.jpg" width="200"/></a><h3>' + a[0].name + " " + str(a[0].price) + '</h3></div>'

        self.coffee_thumb2 = '<div class="product">' + '<a href="?name=' + a[1].name + '"><img src="images/thumb2.jpg" width="200"/></a><h3>' + a[1].name + " " + str(a[1].price) + '</h3></div>'

        self.coffee_thumb3 = '<div class="product">' + '<a href="?name=' + a[2].name + '"><img src="images/thumb3.jpg" width="200"/></a><h3>' + a[2].name + " " + str(a[2].price) + '</h3></div>'

        self.coffee_thumb4 = '<div class="product">' + '<a href="?name=' + a[3].name + '"><img src="images/thumb4.jpg" width="200"/></a><h3>' + a[3].name + " " + str(a[3].price) + '</h3></div>'

        self.coffee_thumb5 = '<div class="product">' + '<a href="?name=' + a[4].name + '"><img src="images/thumb5.jpg" width="200"/></a><h3>' + a[4].name + " " + str(a[4].price) + '</h3></div>'

        self.coffee_thumb_div_close = '</div>'

        self.all_the_coffee += self.coffee_thumb_div + self.coffee_thumb1 + self.coffee_thumb2 + self.coffee_thumb3 + self.coffee_thumb4 + self.coffee_thumb5 + self.coffee_thumb_div_close

    def print_out(self):
        return self.head + self.header + self.main_product + self.all_the_coffee + self.close
