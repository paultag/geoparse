# Copyright (c) Paul Tagliamonte, 2012, under the terms and conditions of the
# COPYING file.


def split_raw(dataset, threshold):
    stop_root = dataset[0]
    onTrip = False
    trip = []
    stop = []
    ret = []
    for item in dataset[1:]:
        delt = abs(item.time - stop_root.time).total_seconds() * threshold
        if (item - stop_root).to_feet() < delt:
            if not onTrip:
                onTrip = True
                ret.append({ "type" : "stop", "data" : stop })
                trip = []
            trip.append(item)
        else:
            if onTrip:
                onTrip = False
                ret.append({ "type" : "trip", "data" : trip })
                stop = []
            stop.append(item)
        stop_root = item
    if onTrip:
        ret.append({ "type" : "trip", "data" : trip })
    else:
        ret.append({ "type" : "stop", "data" : stop })
    return ret
