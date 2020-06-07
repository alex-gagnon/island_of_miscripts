"""Inheritance and abstraction"""

from abc import ABCMeta, abstractmethod


class Vehicle:
    """A vehicle for sale by a local company

    Attributes:
        miles: The integral number of miles driven on the car.
        make: The make of the car as a string.
        model: The model of the car as a string.
        year: The integral year the car was built.
        sold_on: The date the vehicle was sold.
    """
    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__( self, miles, make, model, year, sold_on ):
        """Return a new vehicle object."""
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price( self ):
        """Return the sale price for this car as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price( self ):
        """Return the price for which we would pay to purchase the car."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type( self ):
        """Return a string representing the type of vehicle this is."""
        pass


class Car( Vehicle ):
    """A car for sale."""
    base_sale_price = 8000
    wheels = 4

    def vehicle_type( self ):
        """Return a string representing the type of vehicle this is."""
        return 'car'


class Truck( Vehicle ):
    """A truck for sale."""
    base_sale_price = 10000
    wheels = 4

    def vehicle_type( self ):
        """Return a string representing the type of vehicle this is."""
        return 'truck'


class Motorcycle( Vehicle ):
    base_sale_price = 6000
    wheels = 2

    def vehicle_type( self ):
        """Return a string representing the type of vehicle this is."""
        return 'motorcycle'
