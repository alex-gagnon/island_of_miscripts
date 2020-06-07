class Car:
    wheels = 4  # class attribute, all cars have 4 wheels

    def __init__( self, make, model ):
        self.make = make
        self.model = model

    @staticmethod
    def make_car_sound():
        print( "VRooooooom!" )


class Vehicle:
    wheels = None

    @classmethod
    def is_motorcycle( Car ):
        return Car.wheels == 2


if __name__ == '__main__':
    mustang = Car( 'Ford', 'Mustang' )  # an instance object of the Car class
    print( mustang.wheels )
    mustang.make_car_sound()
