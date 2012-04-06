# Copyright (c) Paul Tagliamonte, 2012, under the terms and conditions of the
# COPYING file.

import datetime as dt
from geoparse.point import Point, PointDelta

d = 123456789
test_time = dt.datetime.fromtimestamp(d)

pd1 = PointDelta(Point(0, 0, d), Point(3, 4, d))
pd2 = PointDelta(Point(0, 0, d), Point(5, 12, d))


def test_create():
    """ Make sure everything's where we expect it to be. """
    point = Point(1, 2, d)
    assert point.lat == 1
    assert point.lon == 2
    assert point.time == test_time


def test_point_eq():
    assert Point(1, 1, d) == Point(1, 1, d)  # Same
    assert Point(1, 1, d) != Point(1, 1, d + 1)  # Different times, same place
    assert Point(2, 1, d) != Point(1, 1, d)  # Different places, same time
    assert Point(2, 1, d) != Point(1, 1, d + 1)  # different everything


def test_subtract():
    """ Test to make sure subtracting two points works right """
    point1 = Point(0.003, 0.004, d)
    point2 = Point(0.000, 0.000, d)
    assert float(point1 - point2) == 0.005
    assert float(point2 - point1) == 0.005


def test_delta_lt():
    """ Ensure less then operator works correctly with numbers & other PDs """
    assert pd1 < pd2
    assert pd1 < 6
    assert pd2 < 14

def test_delta_gt():
    """ Ensure greater then operator works correctly with numbers & other PDs """
    assert pd2 > pd1
    assert pd1 > 4
    assert pd2 > 12

def test_delta_eq():
    """ Ensure equel operator works correctly with numbers & other PDs """
    assert pd1 == 5
    assert pd2 == 13
    assert pd1 == PointDelta(Point(0, 0, d), Point(3, 4, d))
    assert pd2 == PointDelta(Point(0, 0, d), Point(5, 12, d))

def test_delta_ne():
    """ Ensure not equel operator works correctly with numbers & other PDs """
    assert pd1 != pd2
    assert pd1 != None
    assert pd2 != 2

def test_delta_le():
    """ Ensure lt or eq operator works correctly with numbers & other PDs """
    assert pd1 == 5
    assert pd1 <= 5
    assert pd1 <= 6

def test_delta_ge():
    """ Ensure gt or eq operator works correctly with numbers & other PDs """
    assert pd1 == 5
    assert pd1 >= 5
    assert pd1 >= 4

def test_delta_convert():
    p1 = Point(50.0359, -5.4253, d)
    p2 = Point(58.3838, -3.0412, d)
    pd = PointDelta(p1, p2)
    assert int(pd.to_miles()) == 584
    assert int(pd.to_kilometers()) == 940
    assert int(pd.to_feet()) == 3087098
    assert int(pd.to_meters()) == 940947
