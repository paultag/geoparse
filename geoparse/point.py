# Copyright (c) Paul Tagliamonte, 2012, under the terms and conditions of the
# COPYING file.

from geoparse.distance import get_distance, EARTH_MILES, EARTH_KILOM

import datetime as dt
import math


class PointDelta:
    def __init__(self, point1, point2):
        latDelta = point1.lat - point2.lat
        self.latDelta = latDelta

        lonDelta = point1.lon - point2.lon
        self.lonDelta = lonDelta

        self.point1 = point1
        self.point2 = point2

    def to_miles(self):
        return get_distance(self.point1, self.point2, EARTH_MILES)

    def to_kilometers(self):
        return get_distance(self.point1, self.point2, EARTH_KILOM)

    def to_feet(self):
        return self.to_miles() * 5280

    def to_meters(self):
        return self.to_kilometers() * 1000

    def _get_hyp(self):
        return math.sqrt(pow(self.latDelta, 2) + pow(self.lonDelta, 2))

    def __float__(self):
        return self._get_hyp()

    def __lt__(self, other):
        return float(self) < other

    def __gt__(self, other):
        return float(self) > other

    def __eq__(self, other):
        return float(self) == other

    def __ne__(self, other):
        return float(self) != other

    def __le__(self, other):
        return float(self) <= other

    def __ge__(self, other):
        return float(self) >= other

    def __repr__(self):
        return "<PointDelta object, lat delta %s, lon delta %s>" % (
            self.latDelta,
            self.lonDelta
        )


class Point:
    def __init__(self, lat, lon, time):
        self.lat = float(lat)
        self.lon = float(lon)
        self.time = dt.datetime.fromtimestamp(time)

    def __sub__(self, other):
        try:
            return PointDelta(self, other)
        except AttributeError:
            return NotImplemented

    def __eq__(self, other):
        return (self - other) == 0 and (self.time == other.time)

    def __ne__(self, other):
        return (self - other) != 0 or (self.time != other.time)

    def __repr__(self):
       return "<Point object at %s, lat: %s, lon: %s>" % (
           self.time.strftime('%Y-%m-%d %H:%M:%S'),
           self.lat,
           self.lon
       )
