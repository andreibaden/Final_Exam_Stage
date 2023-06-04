from entity.station import Station


# TES - thermal energy station

class TES(Station):
    def __init__(self, thermal_energy=0, thermal_error=0, money=0, energy=0, fail=0):
        super().__init__(money, energy, fail)
        self.__thermal_energy = thermal_energy if \
            isinstance(thermal_energy, (int, float)) and thermal_energy >= 0 else 0
        self.__thermal_error = thermal_error if \
            isinstance(thermal_error, (int, float)) and thermal_error >= 0 else 0

    @property
    def thermal_energy(self):
        return self.thermal_energy

    @thermal_energy.setter
    def thermal_energy(self, thermal_energy):
        if isinstance(thermal_energy, (int, float)) and thermal_energy > 0:
            self.thermal_energy = thermal_energy

    @property
    def thermal_error(self):
        return self.__thermal_error

    @thermal_error.setter
    def thermal_error(self, thermal_error):
        if isinstance(thermal_error, (int, float)) and thermal_error > 0:
            self.thermal_error = thermal_error

    def __str__(self):
        return (f"TES (thermal energy station): "
                f"\n Electric energy = {self.energy} MW, "
                f"\n Thermal energy = {self.__thermal_energy} МCAL, "
                f"\n Thermal error = {self.__thermal_error}, "
                f"\n All logic and function errors = {self.fail}, "
                f"\n Money for investment = {self.money} rub ."
                f"\n")
