# Twig Coding Challenge.

### Requirements(Windows)

------------

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/)

------------ 

### Installation

    > pip install -r requirements.txt
    > pip install virtualenv

### Create and activate environment

    > virtualenv venv
    > venv\Scripts\activate

------------

### Tasks given

Given an array of length >= 0, and a positive integer N, return the contents of the array divided into N equally sized
arrays. Where the size of the original array cannot be divided equally by N, the final part should have a length equal
to the remainder.

           i/p => groupArrayElements([1, 2, 3, 4, 5, 6], 4 );
           o/p => [[1, 2], [3, 4], [5, 6], []]

           i/p => groupArrayElements([ 1 , 2 , 3 , 4 , 5 ], 3 );
           o/p => [ [ 1, 2 ], [ 3, 4 ], [ 5 ] ]

----- 

### Running code

    py main.py

### Script location

[main.py](main.py)

