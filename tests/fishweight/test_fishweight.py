import unittest
import json
from fishweight import fishweight


class FishWeightTest(unittest.TestCase):
    def test_convertibleToFloat_valid_values(self):
        self.assertTrue(fishweight.convertibleToFloat(17))
        self.assertTrue(fishweight.convertibleToFloat(17.0))
        self.assertTrue(fishweight.convertibleToFloat(17.00))
        self.assertTrue(fishweight.convertibleToFloat(28.25))
        self.assertTrue(fishweight.convertibleToFloat(16.5))
        self.assertTrue(fishweight.convertibleToFloat(22.50))
        self.assertTrue(fishweight.convertibleToFloat(44.75))

    def test_convertibleToFloat_invalid_values(self):
        self.assertFalse(fishweight.convertibleToFloat('something'))
        self.assertFalse(fishweight.convertibleToFloat(';$%'))
        self.assertFalse(fishweight.convertibleToFloat(''))
        self.assertFalse(fishweight.convertibleToFloat(None))

    def test_checkArgs_valid_walleye(self):
        fishweight.checkArgs('walleye', '23.25')
        fishweight.checkArgs('walleye', '14')
        fishweight.checkArgs('walleye', '28.5')
        fishweight.checkArgs('walleye', '21.50')
        fishweight.checkArgs('walleye', '16.75')

    def test_checkArgs_valid_northern(self):
        fishweight.checkArgs('northern', '23.25')
        fishweight.checkArgs('northern', '14')
        fishweight.checkArgs('northern', '28.5')
        fishweight.checkArgs('northern', '21.50')
        fishweight.checkArgs('northern', '16.75')

    def test_checkArgs_valid_smallmouth(self):
        fishweight.checkArgs('smallmouth', '23.25')
        fishweight.checkArgs('smallmouth', '14')
        fishweight.checkArgs('smallmouth', '7.5')
        fishweight.checkArgs('smallmouth', '21.50')
        fishweight.checkArgs('smallmouth', '16.75')

    def test_checkArgs_invalid_species(self):
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Small mouth', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs('walleye Pike', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Walleye', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Northern', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Smallmouth', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Pike', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs('', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs(None, '23.25')

    def test_checkArgs_length_valid(self):
        fishweight.checkArgs('walleye', fishweight.WALLEYE_LENGTH_LOWER_LIMIT)
        fishweight.checkArgs('walleye', fishweight.WALLEYE_LENGTH_UPPER_LIMIT)
        fishweight.checkArgs('walleye', 21.00)
        fishweight.checkArgs(
            'northern', fishweight.NORTHERN_LENGTH_LOWER_LIMIT)
        fishweight.checkArgs(
            'northern', fishweight.NORTHERN_LENGTH_UPPER_LIMIT)
        fishweight.checkArgs('northern', 28)
        fishweight.checkArgs(
            'smallmouth', fishweight.SMALLMOUTH_LENGTH_LOWER_LIMIT)
        fishweight.checkArgs(
            'smallmouth', fishweight.SMALLMOUTH_LENGTH_UPPER_LIMIT)
        fishweight.checkArgs('smallmouth', 17.75)

    def test_checkArgs_length_invalid(self):
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'walleye', fishweight.WALLEYE_LENGTH_LOWER_LIMIT-.25)
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'walleye', fishweight.WALLEYE_LENGTH_UPPER_LIMIT+.25)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('walleye', None)
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'northern', fishweight.NORTHERN_LENGTH_LOWER_LIMIT-1)
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'northern', fishweight.NORTHERN_LENGTH_UPPER_LIMIT+1)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('northern', None)
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'smallmouth', fishweight.SMALLMOUTH_LENGTH_LOWER_LIMIT-2.75)
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'smallmouth', fishweight.SMALLMOUTH_LENGTH_UPPER_LIMIT+2.75)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('smallmouth', None)

    def test_checkArgs_length_whole_or_quarter_valid(self):
        fishweight.checkArgs('walleye', 18)
        fishweight.checkArgs('walleye', 18.0)
        fishweight.checkArgs('walleye', 18.00)
        fishweight.checkArgs('walleye', 18.000)
        fishweight.checkArgs('walleye', 18.0000)
        fishweight.checkArgs('walleye', 18.25)
        fishweight.checkArgs('walleye', 18.250)
        fishweight.checkArgs('walleye', 18.2500)
        fishweight.checkArgs('walleye', 18.5)
        fishweight.checkArgs('walleye', 18.50)
        fishweight.checkArgs('walleye', 18.500)
        fishweight.checkArgs('walleye', 18.5000)
        fishweight.checkArgs('walleye', 18.75)
        fishweight.checkArgs('walleye', 18.750)
        fishweight.checkArgs('walleye', 18.7500)

    def test_checkArgs_length_whole_or_quarter_invalid(self):
        with self.assertRaises(ValueError):
            fishweight.checkArgs('walleye', 18.1)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('walleye', 18.26)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('walleye', 18.875)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('walleye', 18.625)

    def test_lengthToWeight_happypaths(self):
        fishweight.lengthToWeight('walleye', '21.5')
        fishweight.lengthToWeight('walleye', '20.500')
        fishweight.lengthToWeight('northern', '22.25')
        fishweight.lengthToWeight('smallmouth', '17.0')


if __name__ == '__main__':
    unittest.main()
