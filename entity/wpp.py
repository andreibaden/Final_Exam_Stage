from entity.station import Station


# wpp - water-power plant

class WPP(Station):
    def __init__(self, hydro_energy=0, hydro_error=0, money=0, energy=0, fail=0):
        super().__init__(money, energy, fail)
        self.__hydro_energy = hydro_energy
        self.__hydro_error = hydro_error

    @property
    def hydro_energy(self):
        return self.hydro_energy

    @hydro_energy.setter
    def hydro_energy(self, hydro_energy):
        self.hydro_energy = hydro_energy

    @property
    def hydro_error(self):
        return self.__hydro_error

    @hydro_error.setter
    def hydro_error(self, hydro_error):
        self.hydro_error = hydro_error

    def __str__(self):
        return (f"WPP (water-power plant): "
                f"\n Electric energy = {self.energy} Мвт, "
                f"\n Hydro energy = {self.__hydro_energy} Мвт, "
                f"\n Hydro error = {self.__hydro_error}, "
                f"\n All logic and function errors = {self.fail}, "
                f"\n Money for investment = {self.money} rub ."
                f"\n")
