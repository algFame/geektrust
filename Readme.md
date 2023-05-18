[//]: # ()
[//]: # (<style>)

[//]: # ()
[//]: # (body {)

[//]: # ()
[//]: # (  background-color: #47546c;)

[//]: # ()
[//]: # (})

[//]: # ()
[//]: # (</style>)

<h1> Ride Sharing </h1>

### <u> Context </u>

<div style="background-color: black; box-shadow: -3px -3px 30px 3px #eee;     padding: 1.4rem;">

[//]: # (<h3> Content </h3>)

Once upon a time, there was a group of entrepreneurs who were busy building a new ride-sharing service. They were working tirelessly to make sure that their service was the best it could be for their riders (i.e passengers) and drivers. However, they knew that there was one important feature missing, the ability to match riders with drivers within a 5km range (inclusive).

One day, they realized that they needed to implement this feature as soon as possible, and they needed someone to take on the challenge of creating it. Can you help them to complete this?

Euclidean Distance Formula
For ease of calculation, this service assumes a Cartesian coordinate system to represent locations, where the location of drivers and riders are represented as a Point(x, y). The Euclidean distance is utilized to calculate the distance between any two points, and 1 unit is equivalent to 1 km.

The Euclidean distance formula says:

`d = √[ (x2–x1)2 + (y2–y1)2]`

where,

(x1, y1) are the coordinates of one point.
(x2, y2) are the coordinates of the other point.
d is the distance between (x1, y1) and (x2, y2).
Goal

_**Your task is to build a solution that will help to match riders with drivers based on their location and generate a bill for the ride.**_

</div>

### <u> Assumptions </u>

<div style="background-color: black; box-shadow: -3px -3px 30px 3px #eee;     padding: 1.4rem;">

It is guaranteed that no two drivers or riders will have the same id.
Ride can only be started once the match is completed.
Every start ride request will happen after the match request.
Every start ride request will have a valid rider id.
One rider can make multiple match requests.
Bill for the ride will be calculated based on the distance between the rider’s location and the destination.
Bill can only be generated after the ride is completed.
The driver will not be available to accept another rider’s request after the ride has started.
Time taken for a ride cannot be negative.
All floating point numerical values must be rounded to two decimal places.

</div>