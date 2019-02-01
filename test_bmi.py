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


def test_categories():
    u = 'underweight'
    n = 'normal'
    o = 'overweight'
    f = 'obese'
    assert u == youFat(17.0)
    assert n == youFat(22)
    assert o == youFat(28.3234)
    assert f == youFat(32)
