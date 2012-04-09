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

Bugs
====

Since this is code I'm working on for chuckles and giggles, and so much of
this stuff is erratic, there is an implied promise that this code is just
littered with all sorts of bugs. Some might be subtle, others might be
tragically apparent.

The ideal bug report will come with a fix, in either a GitHub pull request,
or an emailed format-patch. Either way is perfectly fine.

  * The great bug report will contain some data to showcase the problem, and
    a small addition to the test suite to show that it does, in fact, fail.

  * The good bug report will contain example data, or enough of a description
    to create new data to show the problem.

  * The bad bug report will contain only a complaint.

  * The unacceptable bug report will just contain personal insults.

Please feel free to email me bugs, praise, patches or requests for help,
 - Paul
