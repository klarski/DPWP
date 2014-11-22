class CoffeeTypes(object):
    def __init__(self):
        self.blends_arr = []
        self.add_coffee_array()

    def add_coffee_array(self):
        bb = BrooklynBlend()
        pb = PortlandBlend()
        ab = AustinBlend()
        bost_b = BostonBlend()
        sb = SanFranBlend()

        self.blends_arr.append(bb)
        self.blends_arr.append(pb)
        self.blends_arr.append(ab)
        self.blends_arr.append(bost_b)
        self.blends_arr.append(sb)

        return self.blends_arr

class BrooklynBlend(object):
    def __init__(self):
        self._name = "Brooklyn Blend"
        self.price = 14.99
        self._roast = "Medium-Bold"
        self.regions = "Guatemala, Rwanda"
        self.flavors = "Sweet, Chocolate, Soft nutty"
        self.image = "images/coffee1.jpg"

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
        self.image = "images/coffee2.jpg"

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
        self.image = "images/coffee3.jpg"

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
        self.image = "images/coffee4.jpg"

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
        self.image = "images/coffee5.jpg"

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