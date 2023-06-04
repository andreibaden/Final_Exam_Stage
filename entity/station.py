class Station:
    def __init__(self, money=0, energy=0, fail=0):
        self.__money = money  # money for investment
        self.__energy = energy  # electric energy generated
        self.__fail = fail  # all logic and function error

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        if isinstance(money, (int, float)) and money >= 0:
            self.__money = money

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, energy):
        if isinstance(energy, (int, float)):
            self.__energy = energy

    @property
    def fail(self):
        return self.__fail

    @fail.setter
    def fail(self, fail):
        if isinstance(fail, (int, float)) and fail >= 0:
            self.__fail = fail
