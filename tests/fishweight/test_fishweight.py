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
        fishweight.checkArgs('Walleye', '23.25')
        fishweight.checkArgs('Walleye', '14')
        fishweight.checkArgs('Walleye', '28.5')
        fishweight.checkArgs('Walleye', '21.50')
        fishweight.checkArgs('Walleye', '16.75')

    def test_checkArgs_valid_northern(self):
        fishweight.checkArgs('Northern', '23.25')
        fishweight.checkArgs('Northern', '14')
        fishweight.checkArgs('Northern', '28.5')
        fishweight.checkArgs('Northern', '21.50')
        fishweight.checkArgs('Northern', '16.75')

    def test_checkArgs_valid_smallmouth(self):
        fishweight.checkArgs('Smallmouth', '23.25')
        fishweight.checkArgs('Smallmouth', '14')
        fishweight.checkArgs('Smallmouth', '7.5')
        fishweight.checkArgs('Smallmouth', '21.50')
        fishweight.checkArgs('Smallmouth', '16.75')

    def test_checkArgs_invalid_species(self):
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Small mouth', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Walleye Pike', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs('walleye', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Pike', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs('', '23.25')
        with self.assertRaises(ValueError):
            fishweight.checkArgs(None, '23.25')

    def test_checkArgs_length_valid(self):
        fishweight.checkArgs('Walleye', fishweight.WALLEYE_LENGTH_LOWER_LIMIT)
        fishweight.checkArgs('Walleye', fishweight.WALLEYE_LENGTH_UPPER_LIMIT)
        fishweight.checkArgs('Walleye', 21.00)
        fishweight.checkArgs(
            'Northern', fishweight.NORTHERN_LENGTH_LOWER_LIMIT)
        fishweight.checkArgs(
            'Northern', fishweight.NORTHERN_LENGTH_UPPER_LIMIT)
        fishweight.checkArgs('Northern', 28)
        fishweight.checkArgs(
            'Smallmouth', fishweight.SMALLMOUTH_LENGTH_LOWER_LIMIT)
        fishweight.checkArgs(
            'Smallmouth', fishweight.SMALLMOUTH_LENGTH_UPPER_LIMIT)
        fishweight.checkArgs('Smallmouth', 17.75)

    def test_checkArgs_length_invalid(self):
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'Walleye', fishweight.WALLEYE_LENGTH_LOWER_LIMIT-.25)
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'Walleye', fishweight.WALLEYE_LENGTH_UPPER_LIMIT+.25)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Walleye', None)
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'Northern', fishweight.NORTHERN_LENGTH_LOWER_LIMIT-1)
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'Northern', fishweight.NORTHERN_LENGTH_UPPER_LIMIT+1)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Northern', None)
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'Smallmouth', fishweight.SMALLMOUTH_LENGTH_LOWER_LIMIT-2.75)
        with self.assertRaises(ValueError):
            fishweight.checkArgs(
                'Smallmouth', fishweight.SMALLMOUTH_LENGTH_UPPER_LIMIT+2.75)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Smallmouth', None)

    def test_checkArgs_length_whole_or_quarter_valid(self):
        fishweight.checkArgs('Walleye', 18)
        fishweight.checkArgs('Walleye', 18.0)
        fishweight.checkArgs('Walleye', 18.00)
        fishweight.checkArgs('Walleye', 18.000)
        fishweight.checkArgs('Walleye', 18.0000)
        fishweight.checkArgs('Walleye', 18.25)
        fishweight.checkArgs('Walleye', 18.250)
        fishweight.checkArgs('Walleye', 18.2500)
        fishweight.checkArgs('Walleye', 18.5)
        fishweight.checkArgs('Walleye', 18.50)
        fishweight.checkArgs('Walleye', 18.500)
        fishweight.checkArgs('Walleye', 18.5000)
        fishweight.checkArgs('Walleye', 18.75)
        fishweight.checkArgs('Walleye', 18.750)
        fishweight.checkArgs('Walleye', 18.7500)

    def test_checkArgs_length_whole_or_quarter_invalid(self):
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Walleye', 18.1)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Walleye', 18.26)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Walleye', 18.875)
        with self.assertRaises(ValueError):
            fishweight.checkArgs('Walleye', 18.625)

    def test_lengthToWeight_happypaths(self):
        fishweight.lengthToWeight('Walleye', '21.5')
        fishweight.lengthToWeight('Walleye', '20.500')
        fishweight.lengthToWeight('Northern', '22.25')
        fishweight.lengthToWeight('Smallmouth', '17.0')


if __name__ == '__main__':
    unittest.main()
