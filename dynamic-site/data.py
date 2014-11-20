class CoffeeTypes(object):
    def __init__(self):
        self._name = ""
        self._price = 0
        self._roast = ""
        self._regions = ""
        self._flavors = ""
        self._weight = 16

    @property
    def name(self):
       return self._name


class BrooklynBlend(CoffeeTypes):
    def __init__(self):
        super(CoffeeTypes, self).__init__()
        self._name = "Brooklyn Blend"
        self._price = 14.99
        self._roast = "Medium-Bold"
        self._regions = "Guatemala, Rwanda"
        self._flavors = "Sweet, Chocolate, Soft nutty"


class PortlandBlend(CoffeeTypes):
    def __init__(self):
        super(CoffeeTypes, self).__init__()
        self._name = "Portland Blend"
        self._price = 12.99
        self._roast = "Light"
        self._regions = "Malawi,  Guatemala"
        self._flavors = "Notes of chocolate and berries, citrus marmalade finish"


class AustinBlend(CoffeeTypes):
    def __init__(self):
        super(CoffeeTypes, self).__init__()
        self._name = "Austin Blend"
        self._price = 11.99
        self._roast = "Medium"
        self._regions = "Rwanda, India"
        self._flavors = "spicy, cinnamon, nutmeg"


class BostonBlend(CoffeeTypes):
    def __init__(self):
        super(CoffeeTypes, self).__init__()
        self._name = "Boston Blend"
        self._price = 13.99
        self._roast = "Bold"
        self._regions = "Peru, Columbia"
        self._flavors = "nutty, spicy, floral, fruity"


class SanFranBlend(CoffeeTypes):
    def __init__(self):
        super(CoffeeTypes, self).__init__()
        self._name = "SanFran Blend"
        self._price = 14.99
        self._roast = "Dark"
        self._regions = "Rwanda, Honduras"
        self._flavors = "Chocolate, subtly sweet, floral, fruity"