
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power        
        self.origin = origin

    def use_power(self):
        return f"{self.name} uses their power: {self._power}!"

    def get_power(self):
        return self._power

    def set_power(self, new_power):
        self._power = new_power



class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} flies at {self.flight_speed} km/h!"



class StrongHero(Superhero):
    def __init__(self, name, power, origin, strength_level):
        super().__init__(name, power, origin)
        self.strength_level = strength_level

    def lift(self):
        return f"{self.name} lifts {self.strength_level} tons!"
