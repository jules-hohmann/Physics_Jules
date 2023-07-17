import unittest
import physics
import math
import numpy as np


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
        self.assertEqual(physics.will_it_float(1, 1000), None)
        self.assertEqual(physics.will_it_float(0, 1), ValueError)
        self.assertEqual(physics.will_it_float(1, 0), ValueError)
        self.assertEqual(physics.will_it_float(-1, 1), ValueError)
        self.assertEqual(physics.will_it_float(1, -1), ValueError)

    def test_calculatepressure(self):
        self.assertEqual(physics.calculate_pressure(10), 98100)
        self.assertEqual(physics.calculate_pressure(-1), ValueError)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(10, 2), 5)
        self.assertEqual(physics.calculate_acceleration(1, -1), ValueError)
        self.assertEqual(physics.calculate_acceleration(1, 0), ValueError)

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(6, 3), 2)
        self.assertEqual(physics.calculate_angular_acceleration(1, -1), ValueError)
        self.assertEqual(physics.calculate_angular_acceleration(1, 0), ValueError)

    def test_calculate_moment_of_Inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(2, 2), 8)
        self.assertEqual(physics.calculate_moment_of_inertia(-1, 1), ValueError)
        self.assertEqual(physics.calculate_moment_of_inertia(0, 1), ValueError)
        self.assertEqual(physics.calculate_moment_of_inertia(1, -1), ValueError)

    def test_calculate_auv_acceleration(self):
        self.assertEqual(
            physics.calculate_auv_acceleration(100, math.pi, 100, 0.1, 0.5),
            [-2.0000000000000004, 2.0000000000000004],
        )
        self.assertEqual(
            physics.calculate_auv_acceleration(100, math.pi),
            [-2.0000000000000004, 2.0000000000000004],
        )

    def test_calculate_auv_angular_acceleration(self):
        self.assertEqual(physics.calculate_auv_angular_acceleration(1, math.pi / 2), 2)

    def test_calculate_auv2_acceleration(self):
        self.assertEqual(
            physics.calculate_auv2_acceleration([4, 3, 2, 1], 0, 1), [4, 0]
        )
        self.assertEqual(
            physics.calculate_auv2_acceleration([1, 1, 1, 1], 0, -1), ValueError
        )
        self.assertEqual(physics.calculate_auv2_acceleration([0, 0], 0, 1), ValueError)

    def test_calculate_auv2_angular_acceleration(self):
        self.assertEqual(
            physics.calculate_auv2_angular_acceleration([4, 3, 2, 1], 0, 3, 4, 1),
            40,
        )
        self.assertEqual(
            physics.calculate_auv2_angular_acceleration([1, 1], 0, 0, 0, 1), ValueError
        )
        self.assertEqual(
            physics.calculate_auv2_angular_acceleration([4, 3, 2, 1], 0, 3, 4, 0),
            ValueError,
        )

    def test_simulate_auv2_motion(self):
        output = physics.simulate_auv2_motion([4, 3, 2, 1], 0, 3, 4, 1, 10, 1)

        self.assertEqual(
            np.allclose(output[0], np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])), True
        )
        self.assertEqual(
            np.allclose(output[1], np.array([0, 2, 8, 18, 32, 50, 72, 98, 128, 162])),
            True,
        )
        self.assertEqual(
            np.allclose(output[2], np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), True
        )
        self.assertEqual(
            np.allclose(output[3], np.array([0, 2, 8, 18, 32, 50, 72, 98, 128, 162])),
            True,
        )
        self.assertEqual(
            np.allclose(
                output[4],
                np.array(
                    [
                        [0, 4, 8, 12, 16, 20, 24, 28, 32, 36],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    ]
                ),
            ),
            True,
        )
        self.assertEqual(
            np.allclose(output[5], np.array([0, 4, 8, 12, 16, 20, 24, 28, 32, 36])),
            True,
        )
        self.assertEqual(
            np.allclose(
                output[6],
                np.array(
                    [[0, 4, 4, 4, 4, 4, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                ),
            ),
            True,
        )


if __name__ == "__main__":
    unittest.main()
