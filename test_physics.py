import unittest
import physics


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(1, 1), 9.81)
        self.assertEqual(physics.calculate_buoyancy(0, 1), ValueError)
        self.assertEqual(physics.calculate_buoyancy(1, 0), ValueError)
        self.assertEqual(physics.calculate_buoyancy(-1, 1), ValueError)
        self.assertEqual(physics.calculate_buoyancy(1, -1), ValueError)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(10, 1), True)
        self.assertEqual(physics.will_it_float(1, 1001), False)
        self.assertEqual(physics.will_it_float(1, 1000), True)
        self.assertEqual(physics.will_it_float(0, 1), ValueError)
        self.assertEqual(physics.will_it_float(1, 0), ValueError)
        self.assertEqual(physics.will_it_float(-1, 1), ValueError)
        self.assertEqual(physics.will_it_float(1, -1), ValueError)

    def test_calculatepressure(self):
        self.assertEqual(physics.calculate_pressure(10), 98100)
        self.assertEqual(physics.calculate_pressure(-1), ValueError)


if __name__ == "__main__":
    unittest.main()
