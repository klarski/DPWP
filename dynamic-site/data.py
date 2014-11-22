class CoffeeTypes(object):
    def __init__(self):
        self.blends_arr = []  # this array is going to hold all my coffee blend objects
        self.add_coffee_array()  # calling function that adds data object classes to array

# this is my function that assigns variables to my data object and pushed those objects into the array
    def add_coffee_array(self):
        bb = BrooklynBlend()
        pb = PortlandBlend()
        ab = AustinBlend()
        bost_b = BostonBlend()
        sb = SanFranBlend()

        self.blends_arr.append(bb)  # adding Brooklyn Blend to blends_arr
        self.blends_arr.append(pb)  # adding Portland Blend to blends_arr
        self.blends_arr.append(ab)  # adding Austin Blend to blends_arr
        self.blends_arr.append(bost_b)  # adding Boston Blend to blends_arr
        self.blends_arr.append(sb)  # adding SanFran Blend to blends_arr

        return self.blends_arr  # returning my array

#Class for Data Object: Brooklyn Blend coffee blend
class BrooklynBlend(object):
    def __init__(self):
        self._name = "Brooklyn Blend"
        self.price = 14.99
        self._roast = "Medium-Bold"
        self.regions = "Guatemala, Rwanda"
        self.flavors = "Sweet, Chocolate, Soft nutty"
        self.image = "images/coffee1.jpg"

#getter for name
    @property
    def name(self):
        return self._name

#setter for name
    @name.setter
    def name(self, n):
        self._name = n

#getter for roast
    @property
    def roast(self):
        return self._roast

#setter for roast
    @roast.setter
    def roast(self, rst):
        self._name = rst

#Class for Data Object: Portland Blend coffee blend
class PortlandBlend(object):
    def __init__(self):
        self._name = "Portland Blend"
        self.price = 12.99
        self._roast = "Light"
        self.regions = "Malawi,  Guatemala"
        self.flavors = "Notes of chocolate and berries, citrus marmalade finish"
        self.image = "images/coffee2.jpg"

#getter for name
    @property
    def name(self):
        return self._name

#setter for name
    @name.setter
    def name(self, n):
        self._name = n

#getter for roast
    @property
    def roast(self):
        return self._roast

#setter for roast
    @roast.setter
    def roast(self, rst):
        self._name = rst

#Class for Data Object: Austin Blend coffee blend
class AustinBlend(object):
    def __init__(self):
        self._name = "Austin Blend"
        self.price = 11.99
        self._roast = "Medium"
        self.regions = "Rwanda, India"
        self.flavors = "spicy, cinnamon, nutmeg"
        self.image = "images/coffee3.jpg"

#getter for name
    @property
    def name(self):
        return self._name

#setter for name
    @name.setter
    def name(self, n):
        self._name = n

#getter for roast
    @property
    def roast(self):
        return self._roast

#setter for roast
    @roast.setter
    def roast(self, rst):
        self._name = rst

#Class for Data Object: Boston Blend coffee blend
class BostonBlend(object):
    def __init__(self):
        self._name = "Boston Blend"
        self.price = 13.99
        self._roast = "Bold"
        self.regions = "Peru, Columbia"
        self.flavors = "nutty, spicy, floral, fruity"
        self.image = "images/coffee4.jpg"

#getter for name
    @property
    def name(self):
        return self._name

#setter for name
    @name.setter
    def name(self, n):
        self._name = n

#getter for roast
    @property
    def roast(self):
        return self._roast

#setter for roast
    @roast.setter
    def roast(self, rst):
        self._name = rst

#Class for Data Object: SanFran Blend coffee blend
class SanFranBlend(object):
    def __init__(self):
        self._name = "SanFran Blend"
        self.price = 14.99
        self._roast = "Dark"
        self.regions = "Rwanda, Honduras"
        self.flavors = "Chocolate, subtly sweet, floral, fruity"
        self.image = "images/coffee5.jpg"

#getter for name
    @property
    def name(self):
        return self._name

#setter for name
    @name.setter
    def name(self, n):
        self._name = n

#getter for roast
    @property
    def roast(self):
        return self._roast

#setter for roast
    @roast.setter
    def roast(self, rst):
        self._name = rst