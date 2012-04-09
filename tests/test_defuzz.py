# Copyright (c) Paul Tagliamonte, 2012, under the terms and conditions of the
# COPYING file.

import datetime as dt
from geoparse.point import Point
from geoparse.defuzz import defuzz_raw, defuzz_feet, defuzz_meters, \
                            rolling_average


d = 1234567890
delt = 3 # if it's outside this, per second.


def test_defuzz_single():
    """ Test a single defuzz """
    dataset = [
        Point(0, 0, d),
        Point(1, 1, d + 1),
        Point(0, 0, d + 2),
        Point(-1, -1, d + 3),
        Point(0, 0, d + 6),
        Point(10, 10, d + 8),  # Bad (5)
        Point(0, 0, d + 10),
        Point(0, 0, d + 30),
        Point(0, 0, d + 31)
    ]
    foo = dataset[:]
    del foo[5]
    assert defuzz_raw(dataset, delt) == foo


def test_defuzz_double():
    """ Test a double-defuzz """
    dataset = [
        Point(0, 0, d),
        Point(1, 1, d + 1),
        Point(0, 0, d + 2),
        Point(-1, -1, d + 3),
        Point(0, 0, d + 6),
        # Begin chopped displacement
        Point(10, 10, d + 7),
        Point(10, 10, d + 8),
        Point(10, 10, d + 9),
        Point(10, 10, d + 10),
        # End.
        Point(0, 0, d + 29),
        Point(0, 0, d + 30),
        Point(0, 0, d + 31)
    ]
    foo = dataset[:]
    assert defuzz_raw(dataset, delt) == foo
    foo2 = [
        Point(0, 0, d),
        Point(0, 0, d + 2),
        Point(0, 0, d + 6),
        Point(10, 10, d + 7),
        Point(10, 10, d + 8),
        Point(10, 10, d + 9),
        Point(10, 10, d + 10),
        Point(0, 0, d + 29),
        Point(0, 0, d + 30),
        Point(0, 0, d + 31)
    ]
    # such a hack
    assert defuzz_feet(dataset, delt) == foo2
    assert defuzz_meters(dataset, delt) == foo2



def test_rolling_average():
    """ Test to make sure the avgr works """
    dataset = [
        Point(0, 0, d),
        Point(1, 1, d),
        Point(2, 2, d),
        Point(3, 3, d),
        Point(4, 4, d),
        Point(5, 5, d),
        Point(6, 6, d),
        Point(7, 7, d),
        Point(8, 8, d),
        Point(9, 9, d),
        Point(10, 10, d + 3),
        Point(11, 11, d),
        Point(12, 12, d)
    ]
    testPoint = rolling_average(dataset, 2)
    myPoint = Point(11.5, 11.5, d)
    assert testPoint == myPoint
    testPoint = rolling_average(dataset, 3)
    myPoint = Point(11, 11, (d + 1))
    assert testPoint == myPoint
