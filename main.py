from entity.tes import TES
from entity.dss import DSS
from entity.wpp import WPP
from region_office.region_report import RegReport
from head_office.head_report import HeadReport


def main():
    region_report = RegReport()

    tes1 = TES(0, 0, 0, 0, 0)
    dss1 = DSS(-550, -5400, -789000, -7)
    wpp1 = WPP(88, 4, 2, 8, 4)
    tes2 = TES(125600, 5, 689000, 78900, 43)
    dss2 = DSS(860, 4500, 7800, 8)
    wpp2 = WPP(77000, 4, 90000, 35000, 17)

    region_report.add(tes1)
    region_report.add(dss1)
    region_report.add(wpp1)
    region_report.add(tes2)
    region_report.add(dss2)
    region_report.add(wpp2)

    print(region_report)

    total_money = HeadReport.calculate_total_invest(region_report)
    sum_energy = HeadReport.calculate_total_energy(region_report)

    print(f"______________________________________________"
          f"\nTotal money for investment is {total_money} rub."
          f"\nTotal generated energy is {sum_energy} Мвт."
          f"\n______________________________________________")


if __name__ == "__main__":
    main()
