from main import *
import math
import pytest


def test_calcBMI_metric():
    answer = calcBMI(60, 'kg', 1.65, 'm')
    expected = 22.03
    assert math.isclose(answer, expected, rel_tol=.02)


def test_calcBMI_english():
    answer = calcBMI(132, 'lbs', 65, 'in')
    expected = 22.03
    assert math.isclose(answer, expected, rel_tol=.02)


@pytest.mark.parametrize("bmi, expected", [(14, 'underweight'),
                                           (23.23, 'normal'), (26.765433,
                                           'overweight'), (31.0, 'obese')])
def test_categories(bmi, expected):
    assert youFat(bmi) == expected
