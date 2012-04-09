GeoParse
=========

This library's job is simple - add decent support to Python to handle processing
geo-location data in a sane way.

This is mostly to deal with importing data from GPS transmitters, such as
Google Latitude. Some of the stuff in here is to deal with the sad reality
that our GPS data is, well, crap. Hopefully, this will make cleaning the data
up on import time easier.

In the end, this library should have the following features in place:


  * Clean incoming data to get rid of eratic reports.

  * Split the backlog of data into "stops" and "trips".

  * Detect how similar two trips are

  * Predict (using past trips) when a live data stream is expected to get to
    a given point on the trip, given a similar historical trip.

  * Figure out how far two points are from each other on the earth in meters,
    feet, or any ole' units.
