
import datetime as dt
import math


class PointDelta:
    def __init__(self, latDelta, lonDelta):
        self.latDelta = latDelta
        self.lonDelta = lonDelta

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
            dLat = other.lat - self.lat
            dLon = other.lon - self.lon
            return PointDelta(dLat, dLon)
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
