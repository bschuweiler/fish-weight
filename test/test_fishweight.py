import pytest
import json
from fish_weight import fishweight


def test_convertibleToFloat_valid_values():
    assert fishweight.convertibleToFloat(17) is True
    assert fishweight.convertibleToFloat(17.0) is True
    assert fishweight.convertibleToFloat(17.00) is True
    assert fishweight.convertibleToFloat(28.25) is True
    assert fishweight.convertibleToFloat(16.5) is True
    assert fishweight.convertibleToFloat(22.50) is True
    assert fishweight.convertibleToFloat(44.75) is True


def test_convertibleToFloat_invalid_values():
    assert fishweight.convertibleToFloat('something') is False
    assert fishweight.convertibleToFloat(';$%') is False
    assert fishweight.convertibleToFloat('') is False
    assert fishweight.convertibleToFloat(None) is False


def test_checkArgs_valid_walleye():
    fishweight.checkArgs('walleye', '23.25')
    fishweight.checkArgs('walleye', '14')
    fishweight.checkArgs('walleye', '28.5')
    fishweight.checkArgs('walleye', '21.50')
    fishweight.checkArgs('walleye', '16.75')


def test_checkArgs_valid_northern():
    fishweight.checkArgs('northern', '23.25')
    fishweight.checkArgs('northern', '14')
    fishweight.checkArgs('northern', '28.5')
    fishweight.checkArgs('northern', '21.50')
    fishweight.checkArgs('northern', '16.75')


def test_checkArgs_valid_smallmouth():
    fishweight.checkArgs('smallmouth', '23.25')
    fishweight.checkArgs('smallmouth', '14')
    fishweight.checkArgs('smallmouth', '7.5')
    fishweight.checkArgs('smallmouth', '21.50')
    fishweight.checkArgs('smallmouth', '16.75')


def test_checkArgs_invalid_species():
    with pytest.raises(ValueError, match=r".*Species is not one of .*"):
        fishweight.checkArgs('Small mouth', '23.25')
    with pytest.raises(ValueError, match=r".*Species is not one of .*"):
        fishweight.checkArgs('walleye Pike', '23.25')
    with pytest.raises(ValueError, match=r".*Species is not one of .*"):
        fishweight.checkArgs('Walleye', '23.25')
    with pytest.raises(ValueError, match=r".*Species is not one of .*"):
        fishweight.checkArgs('Northern', '23.25')
    with pytest.raises(ValueError, match=r".*Species is not one of .*"):
        fishweight.checkArgs('Smallmouth', '23.25')
    with pytest.raises(ValueError, match=r".*Species is not one of .*"):
        fishweight.checkArgs('Pike', '23.25')
    with pytest.raises(ValueError, match=r".*Species is not one of .*"):
        fishweight.checkArgs('', '23.25')
    with pytest.raises(ValueError, match=r".*Species is not one of .*"):
        fishweight.checkArgs(None, '23.25')


def test_checkArgs_length_valid():
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


def test_checkArgs_length_invalid():
    with pytest.raises(ValueError,
                       match=r".*Length argument is outside "
                       "reasonable bounds of.*"):
        fishweight.checkArgs(
            'walleye', fishweight.WALLEYE_LENGTH_LOWER_LIMIT-.25)
    with pytest.raises(ValueError,
                       match=r".*Length argument is outside "
                       "reasonable bounds of.*"):
        fishweight.checkArgs(
            'walleye', fishweight.WALLEYE_LENGTH_UPPER_LIMIT+.25)
    with pytest.raises(ValueError,
                       match=r".*Length argument is not a number.*"):
        fishweight.checkArgs('walleye', None)
    with pytest.raises(ValueError,
                       match=r".*Length argument is outside "
                       "reasonable bounds of.*"):
        fishweight.checkArgs(
            'northern', fishweight.NORTHERN_LENGTH_LOWER_LIMIT-1)
    with pytest.raises(ValueError,
                       match=r".*Length argument is outside "
                       "reasonable bounds of.*"):
        fishweight.checkArgs(
            'northern', fishweight.NORTHERN_LENGTH_UPPER_LIMIT+1)
    with pytest.raises(ValueError,
                       match=r".*Length argument is not a number.*"):
        fishweight.checkArgs('northern', None)
    with pytest.raises(ValueError,
                       match=r".*Length argument is outside "
                       "reasonable bounds of.*"):
        fishweight.checkArgs(
            'smallmouth', fishweight.SMALLMOUTH_LENGTH_LOWER_LIMIT-2.75)
    with pytest.raises(ValueError,
                       match=r".*Length argument is outside "
                       "reasonable bounds of.*"):
        fishweight.checkArgs(
            'smallmouth', fishweight.SMALLMOUTH_LENGTH_UPPER_LIMIT+2.75)
    with pytest.raises(ValueError,
                       match=r".*Length argument is not a number.*"):
        fishweight.checkArgs('smallmouth', None)


def test_checkArgs_length_whole_or_quarter_valid():
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


def test_checkArgs_length_whole_or_quarter_invalid():
    with pytest.raises(ValueError,
                       match=r".*Length argument is not "
                       "whole or quarter value.*"):
        fishweight.checkArgs('walleye', 18.1)
    with pytest.raises(ValueError,
                       match=r".*Length argument is not "
                       "whole or quarter value.*"):
        fishweight.checkArgs('walleye', 18.26)
    with pytest.raises(ValueError,
                       match=r".*Length argument is not "
                       "whole or quarter value.*"):
        fishweight.checkArgs('walleye', 18.875)
    with pytest.raises(ValueError,
                       match=r".*Length argument is not "
                       "whole or quarter value.*"):
        fishweight.checkArgs('walleye', 18.625)


def test_lengthToWeight_happypaths():
    fishweight.lengthToWeight('walleye', '21.5')
    fishweight.lengthToWeight('walleye', '20.500')
    fishweight.lengthToWeight('northern', '22.25')
    fishweight.lengthToWeight('smallmouth', '17.0')
