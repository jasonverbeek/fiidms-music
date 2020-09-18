from unittest import TestCase
from package.foo import convert_num


class FooTest(TestCase):

    def test_convert_num(self):
        milligrams = 2578000
        grams = convert_num(num=milligrams, step=1000)
        kilograms_from_gr = convert_num(num=grams, step=1000)
        kilograms_from_mg = convert_num(num=milligrams, step=10**6)
        self.assertEqual(kilograms_from_gr, kilograms_from_mg)
        self.assertEqual(kilograms_from_mg, 2.578)
