from entity.station import Station


# distribution substation with solar panels

class DSS(Station):
    def __init__(self, electric_loss=0, money=0, energy=0, fail=0):
        super().__init__(money, energy, fail)
        self.__electric_loss = electric_loss if \
            isinstance(electric_loss, (int, float)) and electric_loss >= 0 else 0

    @property
    def electric_loss(self):
        return self.electric_loss

    @electric_loss.setter
    def electric_loss(self, electric_loss):
        if isinstance(electric_loss, (int, float)) and electric_loss > 0:
            self.__electric_loss = electric_loss


    def __str__(self):
        return (f"DSS (distribution substation): "
                f"\n Electric energy = {self.energy} МW, "
                f"\n Electric_loss = {self.__electric_loss} MW, "
                f"\n All logic and function errors = {self.fail}, "
                f"\n Money for investment = {self.money} rub ."
                f"\n")
