"""
 Continued fractions

 AUTHORS:

 K.Draziotis (26-5-2015): initial version



 TESTS: conf(22,23)
        [0,1,22]
        
        conv(22,23)
        [0,1,22/23]


 REFERENCES: The joy of factoring, S.S.Wagstaff, Jr. AMS
 
"""


#*****************************************************************************
#       Copyright (C) 2015 K.Draziotis <drazioti@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


import math
import mpmath
from sympy.mpmath import *
from sympy import Rational
from mpmath import *
from mpmath import mp
mp.dps=800;
def conf(a,b):
    i=0
    q1=[]
    q1.append(Rational(0,1))
    x=Rational(int(a),int(b))
    q=Rational(int(floor(x)),int(1))
    x=x-q
    while(x>0):
        q1.append(int(floor(Rational(1,x))))
        x=1/x-q1[i+1]
        i=i+1
    return q1

### convergent by classical theorems
def P(n,a,b):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return conf(a,b)[n-1]*P(n-1,a,b)+P(n-2,a,b)
### convergent by classical theorems
def Q(n,a,b):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return conf(a,b)[n-1]*Q(n-1,a,b)+Q(n-2,a,b)
### convergent -- very slow
def conv(a,b):
    c=[];i=0;
    for i in range(len(conf(a,b))):
        c.append(Rational(P(i+1,a,b),Q(i+1,a,b)))
    return c
