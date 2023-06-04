import unittest
from entity.tes import TES


class TESTest(unittest.TestCase):
    def test_tes_default_constructor(self):
        tes = TES()
        expected_thermal_energy = 0
        expected_thermal_error = 0
        expected_money = 0
        expected_energy = 0
        expected_fail = 0

        self.assertEqual(expected_thermal_energy, tes.thermal_energy)
        self.assertEqual(expected_thermal_error, tes.thermal_error)
        self.assertEqual(expected_money, tes.money)
        self.assertEqual(expected_energy, tes.energy)
        self.assertEqual(expected_fail, tes.fail)

    def test_tes_constructor_with_args(self):
        exp_thermal_energy = 90
        exp_thermal_error = 17
        exp_money = 1000
        exp_energy = 5000
        exp_fail = 10

        tes = TES(exp_thermal_energy, exp_thermal_error, exp_money,
                  exp_energy, exp_fail)

        self.assertEqual(exp_thermal_energy, tes.thermal_energy)
        self.assertEqual(exp_thermal_error, tes.thermal_error)
        self.assertEqual(exp_money, tes.money)
        self.assertEqual(exp_energy, tes.energy)
        self.assertEqual(exp_fail, tes.fail)

    def test_negative_tes_thermal_energy(self):
        thermal_energy = -20
        expected = 0

        tes = TES(thermal_energy=thermal_energy)

        self.assertEqual(expected, tes.thermal_energy)

    def test_negative_tes_thermal_error(self):
        thermal_error = -2
        expected = 0

        tes = TES(thermal_error=thermal_error)

        self.assertEqual(expected, tes.thermal_error)

    def test_negative_tes_money(self):
        money = -8
        expected = 0

        tes = TES(money=money)

        self.assertEqual(expected, tes.money)

    def test_negative_tes_energy(self):
        energy = -9
        expected = 0

        tes = TES(energy=energy)

        self.assertEqual(expected, tes.energy)

    def test_negative_tes_fail(self):
        fail = -3
        expected = 0

        tes = TES(fail=fail)

        self.assertEqual(expected, tes.fail)

    def test_zero_tes_thermal_energy(self):
        thermal_energy = 0
        expected = 0

        tes = TES(thermal_energy=thermal_energy)

        self.assertEqual(expected, tes.thermal_energy)

    def test_zero_tes_thermal_error(self):
        thermal_error = 0
        expected = 0

        tes = TES(thermal_error=thermal_error)

        self.assertEqual(expected, tes.thermal_error)

    def test_zero_tes_money(self):
        money = 0
        expected = 0

        tes = TES(money=money)

        self.assertEqual(expected, tes.money)

    def test_zero_tes_energy(self):
        energy = 0
        expected = 0

        tes = TES(energy=energy)

        self.assertEqual(expected, tes.energy)

    def test_zero_tes_fail(self):
        fail = 0
        expected = 0

        tes = TES(fail=fail)

        self.assertEqual(expected, tes.fail)

    def test_thermal_energy_property_negative(self):
        tes = TES()
        expected = tes.thermal_energy
        tes.thermal_energy = -30
        self.assertEqual(expected, tes.thermal_energy)

    def test_thermal_energy_property_positive(self):
        tes = TES()
        expected = 100
        tes.thermal_energy = 100
        self.assertEqual(expected, tes.thermal_energy)

    def test_thermal_energy_property_with_zero(self):
        tes = TES()
        expected = tes.thermal_energy
        tes.thermal_energy = 0
        self.assertEqual(expected, tes.thermal_energy)

    def test_thermal_error_property_negative(self):
        tes = TES()
        expected = tes.thermal_error
        tes.thermal_error = -30
        self.assertEqual(expected, tes.thermal_error)

    def test_thermal_error_property_positive(self):
        tes = TES()
        expected = 100
        tes.thermal_error = 100
        self.assertEqual(expected, tes.thermal_error)

    def test_thermal_error_property_with_zero(self):
        tes = TES()
        expected = tes.thermal_error
        tes.thermal_error = 0
        self.assertEqual(expected, tes.thermal_error)


if __name__ == "__main__":
    unittest.main()
