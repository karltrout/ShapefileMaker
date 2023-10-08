import math
from unittest import TestCase

import main


class Test(TestCase):
    def test_dms2dd(self):
        result = main.dms2dd("38104763N")
        self.assertAlmostEqual(result, 38.179897, 3)
        result = main.dms2dd("077060000W")
        self.assertAlmostEqual(result, -77.1, 3)
        result = main.dms2dd("077060010W")
        self.assertAlmostEqual(result, -77.1, 3 )
        result = main.dms2dd("xyz")
        assert(math.isnan(result))
        result = main.dms2dd(42.0)
        assert math.isnan(result)
