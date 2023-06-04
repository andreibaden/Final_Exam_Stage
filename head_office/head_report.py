from entity.station import Station
from region_office.region_report import RegReport


class HeadReport:
    @staticmethod
    def calculate_total_invest(region_report):
        if isinstance(region_report, RegReport) and region_report.size != 0:
            total = 0
            for i in range(region_report.size):
                station = region_report.get_station(i)

                if isinstance(station, Station):
                    total += station.money

            return total
        else:
            return 0

    @staticmethod
    def calculate_total_energy(region_report):
        if isinstance(region_report, RegReport) and region_report.size != 0:
            total = 0
            for i in range(region_report.size):
                station = region_report.get_station(i)

                if isinstance(station, Station):
                    total += station.energy

            return total
        else:
            return 0
