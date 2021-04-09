# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *


class TestLocation(unittest.TestCase):

    def test_repr(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

    def test_init(self):
        loc = Location('Porterville', 36.07, 119.02)
        self.assertEqual(loc.name, 'Porterville')
        self.assertEqual(loc.lat, 36.07)
        self.assertEqual(lopc.lon, 119.02)

    def test_eq(self):
        loc1 = Location('Porterville', 36.07, 119.02)
        loc2 = Location('Fresno', 36.74, 119.79)
        loc3 = Location('Porterville', 36.07, 119.02)
        loc4 = loc3
        loc5 = [7]
        self.assertEqual(loc4, loc3)
        self.assertNotEqual(loc3, loc2)
        self.assertEqual(loc4, loc1)
        self.assertFalse(loc3.__eq__(loc2))
        self.assertTrue(loc3.__eq__(loc1))



if __name__ == "__main__":
    unittest.main()
