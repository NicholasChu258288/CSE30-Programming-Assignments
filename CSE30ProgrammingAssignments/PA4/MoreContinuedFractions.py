#------------------------------------------------------------------------------
#  Nicholas  Chu
#  1790585
#  CSE 30-02 Spring 2021
#  lab3
#  MoreContinuedFractions.py
#  Adds more functions that involve continued fractions, also for the purpose of
#  getting a rational representation of pi to 100 decimal places
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# import statements
#------------------------------------------------------------------------------
from decimal import *
from rational import *

#------------------------------------------------------------------------------
# definitions of optional helper functions
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# definitions of required functions, classes etc.
#------------------------------------------------------------------------------
def CF2R(L):
    # a recursive fucntion that takes an input list, L, and returns a Rational
    # object representing the corresponding continued fraction as a rational number
    num = L.pop(0)
    if len(L) >= 1:
        return Rational(num, 1) + Rational(1, 1) / CF2R(L)
    if len(L) == 0:
        return Rational(num, 1)
#end

def R2CF(x):
    #inverse of CF2R where it takes ration number as input (x) then returns a list
    #representing the continued fraction
    CF_to_list = []
    a = x.numer
    b = x.denom
    #print(x.numer,x.denom) #when testing to see what R2CF is doing
    #print(a,b) #when testing to see what R2CF is doing
    CF_to_list.append(a//b)

    while b:
        c = a  #c is just a placeholder when replacing
        a = b
        b = c % b
        #print(a, b) #when testing to see what R2CF is doing
        if b != 0:
            CF_to_list.append(a//b)
    #end
    return CF_to_list
#end

def GCF2R(L):
    #that takes a list L (of odd length) representing a generalized continued fraction,
    #then returns the corresponding rational number as an object of type Rational

    #Some conditionals
    #special case if list is empty
    if len(L) == 0:
        return Rational(1)
    if len(L) >= 2:
        num1 = L.pop(0)
        num2 = L.pop(0)
        return Rational(num1) + Rational(num2)/ GCF2R(L)
    if len(L) == 1:
        num = L.pop(0)
        return Rational(num)
#end

def pi_gen():
    #First hundred digits of pi:
    #3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    k = 1
    yield 0
    yield 4
    while True:
        yield 2*k-1
        yield k**2
        k += 1
#end


#------------------------------------------------------------------------------
# if this is a stand alone module, i.e. not a program to be run, then you can
# stop here. If this is a program to be run under python, then continue.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# definition of function main()
#------------------------------------------------------------------------------
def main():
    getcontext().prec = 101

    g = pi_gen()
    x = []
    for i in range(268):  # fill range with how long you want list to be
        x.append(next(g))  # x would be the list by that you want to use, not a generator object
    hundred_decimal_pi = GCF2R(x)
    print('')
    print(hundred_decimal_pi)
    print('')
    print(Decimal(hundred_decimal_pi.numer) / Decimal(hundred_decimal_pi.denom))
    print('')
    print(R2CF(hundred_decimal_pi))
    print('')

#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
if __name__ == '__main__':

    main()

#end