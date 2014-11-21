class CoffeeTypes(object):
    def __init__(self):
        bb = BostonBlend()
        pb = PortlandBlend()
        ab = AustinBlend()
        bost_b = BostonBlend()
        sb = SanFranBlend()



class BrooklynBlend(object):
    def __init__(self):
        self._name = "Brooklyn Blend"
        self.price = 14.99
        self._roast = "Medium-Bold"
        self.regions = "Guatemala, Rwanda"
        self.flavors = "Sweet, Chocolate, Soft nutty"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def roast(self):
        return self._roast

    @roast.setter
    def roast(self, rst):
        self._name = rst


class PortlandBlend(object):
    def __init__(self):
        self._name = "Portland Blend"
        self.price = 12.99
        self._roast = "Light"
        self.regions = "Malawi,  Guatemala"
        self.flavors = "Notes of chocolate and berries, citrus marmalade finish"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def roast(self):
        return self._roast

    @roast.setter
    def roast(self, rst):
        self._name = rst


class AustinBlend(object):
    def __init__(self):
        self._name = "Austin Blend"
        self.price = 11.99
        self._roast = "Medium"
        self.regions = "Rwanda, India"
        self.flavors = "spicy, cinnamon, nutmeg"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def roast(self):
        return self._roast

    @roast.setter
    def roast(self, rst):
        self._name = rst


class BostonBlend(object):
    def __init__(self):
        self._name = "Boston Blend"
        self.price = 13.99
        self._roast = "Bold"
        self.regions = "Peru, Columbia"
        self.flavors = "nutty, spicy, floral, fruity"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def roast(self):
        return self._roast

    @roast.setter
    def roast(self, rst):
        self._name = rst


class SanFranBlend(object):
    def __init__(self):
        self._name = "SanFran Blend"
        self.price = 14.99
        self._roast = "Dark"
        self.regions = "Rwanda, Honduras"
        self.flavors = "Chocolate, subtly sweet, floral, fruity"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def roast(self):
        return self._roast

    @roast.setter
    def roast(self, rst):
        self._name = rst