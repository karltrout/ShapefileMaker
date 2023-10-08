from unittest import TestCase

import main
import math


class Test(TestCase):
    def test_dms2dd(self):
        result = main.dms2dd("42330000N")
        self.assertEqual(result, 42.55)
        result = main.dms2dd("077060000W")
        self.assertEqual(result, -77.1)
        result = main.dms2dd("xyz")
        assert(math.isnan(result))
