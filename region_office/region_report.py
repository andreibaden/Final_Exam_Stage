from entity.station import Station


class RegReport:
    def __init__(self, stations=None):
        self.__stations = stations
        if stations:
            self.__stations = stations
        else:
            self.__stations = []

    @property
    def size(self):
        return len(self.__stations)

    def get_station(self, index):
        if (isinstance(index, int) and index >= 0 and index < self.size):
            return self.__stations[index]

    def add(self, station):
        if isinstance(station, Station):
            self.__stations.append(station)

    def __str__(self):
        msg = "\n List of stations:"

        for i in range(self.size):
            msg += f"\n{i + 1}) " + str(self.__stations[i])

        return msg
