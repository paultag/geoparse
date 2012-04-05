#

from geoparse.point import Point
import geoparse.distance

d = 1234567890

def test_distance_km():
    p1 = Point(50.0359, -5.4253, d)
    p2 = Point(58.3838, -3.0412, d)
    distance = geoparse.distance.get_distance(p1, p2,
                                         geoparse.distance.EARTH_KILOM)
    assert int(distance) == 940
    distance = geoparse.distance.get_distance(p1, p2,
                                         geoparse.distance.EARTH_MILES)
    assert int(distance) == 584
