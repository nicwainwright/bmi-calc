from main import *
import math
import pytest


@pytest.mark.parametrize("weight, weight_unit, height, height_unit",
                         [(60, 'kg', 1.65, 'm'), (132, 'lbs', 65, 'in')])
def test_calcBMI(weight, weight_unit, height, height_unit):
    answer = calcBMI(weight, weight_unit, height, height_unit)
    expected = 22.03
    assert math.isclose(answer, expected, rel_tol=.02)


@pytest.mark.parametrize("bmi, expected", [(14, 'underweight'),
                                           (23.23, 'normal'), (26.765433,
                                           'overweight'), (31.0, 'obese')])
def test_categories(bmi, expected):
    assert youFat(bmi) == expected
