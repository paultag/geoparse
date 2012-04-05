# Copyright (c) Paul Tagliamonte, 2012, under the terms and conditions of the
# COPYING file.

from geoparse.point import Point
import datetime as dt

def defuzz(dataset, change):
    """
    Expecting a list of points to defuzz.

    change should be a number, the change in lat/lon per second. If it's past
    this value, it's going to be snipped, providing it's past this threshold
    on *both* sides.
    """
    # XXX: Change this to use feet, not change in lat/lon directly.
    index = 1
    while index < (len(dataset) - 1):
        pre = dataset[index - 1]
        cur = dataset[index]
        post = dataset[index + 1]

        preDeltP = (cur - pre)
        preDeltT = (cur.time - pre.time)

        postDeltP = (post - cur)
        postDeltT = (post.time - cur.time)

        preDeltThr = (change * preDeltT.total_seconds())
        postDeltThr = (change * postDeltT.total_seconds())

        if preDeltP > preDeltThr and postDeltP > postDeltThr:
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
