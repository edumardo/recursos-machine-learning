# Imports

import math
print(dir(math))                        # We can see all the names in math using dir()
print("pi = {:.4}".format(math.pi))     # Dot syntax

import math as mt                       # Import under a shorter alias
mt.pi

from math import *                      # Makes all the module's variables directly accessible
from numpy import *                     # math and mumpy have both log function
print(pi, log(32, 2))                   # error!

from math import log, pi                # Good compromise
from numpy import asarray               # Import only the specific things we'll need

import numpy                            # numpy has a variable referring other module: two dots syntax
rolls = numpy.random.randint(low=1, high=6, size=10)

# Three tools for understanding strange objects

type(rolls)                             # What is this thing?
dir(rolls)                              # What can I do with it?
help()                                  # Tell me more
