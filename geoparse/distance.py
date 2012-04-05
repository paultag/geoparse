# Copyright (c) Paul Tagliamonte, 2012, under the terms and conditions of the
# COPYING file.

import math

EARTH_KILOM = 6371
EARTH_MILES = 3958.7558657440545
# Radius of the earth.

def to_rad(val):
    # XXX: testme
    return val * math.pi / 180;

def get_distance(point1, point2, radius):
    """ This is called the "haversine" formula. """
    pDelt = (point2 - point1)
    dLat = to_rad(pDelt.latDelta)
    dLon = to_rad(pDelt.lonDelta)
    a = math.sin(float(dLat) / 2) * math.sin(float(dLat) / 2) + \
        math.cos(to_rad(point1.lat)) * math.cos(to_rad(point2.lat)) * \
        math.sin(float(dLon) / 2) * math.sin(float(dLon) / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d
