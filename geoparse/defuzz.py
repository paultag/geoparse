# Copyright (c) Paul Tagliamonte, 2012, under the terms and conditions of the
# COPYING file.

from geoparse.point import Point
import datetime as dt

def raw_cmpr(change, pre, cur, post):
    preDeltP = (cur - pre)
    preDeltT = (cur.time - pre.time)
    postDeltP = (post - cur)
    postDeltT = (post.time - cur.time)
    preDeltThr = (change * preDeltT.total_seconds())
    postDeltThr = (change * postDeltT.total_seconds())
    return preDeltP > preDeltThr and postDeltP > postDeltThr


def feet_cmpr(change, pre, cur, post):
    preD = (cur - pre)
    postD = (cur - post)
    return preD.to_feet() > change and postD.to_feet() > change


def meter_cmpr(change, pre, cur, post):
    preD = (cur - pre)
    postD = (cur - post)
    return preD.to_meters() > change and postD.to_meters() > change

# End compare functions. Goodies below

def defuzz_raw(dataset, change):
    return defuzz_data(dataset, change, raw_cmpr)


def defuzz_feet(dataset, change):
    return defuzz_data(dataset, change, feet_cmpr)


def defuzz_meters(dataset, change):
    return defuzz_data(dataset, change, meter_cmpr)


def defuzz_data(dataset, change, cmpr):
    index = 1
    while index < (len(dataset) - 1):
        pre = dataset[index - 1]
        cur = dataset[index]
        post = dataset[index + 1]
        if cmpr(change, pre, cur, post):
            del dataset[index]
            if index > 6:
                index = index - 5
            else:
                index = 1
        index += 1
    return dataset


def rolling_average(dataset, howmany):
    """
    Expecting a list of points to defuzz from dataset
    Expecting the count of the last N to defuzz.
    """
    dataset = dataset[-howmany:]
    total = 0
    totalLat = 0
    totalLon = 0
    totalTime = 0
    for point in dataset:
        total += 1
        totalLat += point.lat
        totalLon += point.lon
        totalTime += float(point.time.strftime("%s"))
    ret = Point((totalLat / total), (totalLon / total),
                totalTime / total)
    return ret
