#------------------------------------------------------------------------------
#  Nicholas  Chu
#  1790585
#  CSE 30-02 Spring 2021
#  pa4
#  rational.py
#  The Rational class will encapsulate these two integers, and define 18 functions,
#  implementing rational arithmetic in terms of pure integer arithmetic.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# import statements
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# definitions of optional helper functions
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# definitions of required functions, classes etc.
#------------------------------------------------------------------------------
class Rational(object):
    """Class representing a rational number."""

    def __init__(self, n, d=1):
        '''Initialize a Rational object'''
        self.numerator = n
        self.denominator = d
        #Gets the GCD if the rational number object
        gcd = Rational._gcd(self, self.numerator, self.denominator)
        #Divides the GCD from the numerator and denominator to produce the simplified rational number
        #Will return 1 if it cannot be simplified anymore
        #Using floor division here just so the numerator and deominator dont get turned into floats due to biohavior of
        #of division operator
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd

        if self.denominator == 0:
            raise ZeroDivisionError
        if self.denominator <= 0:
            #used to always make that denominator is positive
            #this makes it eaiser to compare in the __eq__ overload
            self.denominator *= -1
            self.numerator *= -1

    def _gcd(self, a, b):
        '''Returns the GCD of a and b.'''
        #A recursive version of Euclid's algorithm to find GCD between a and b
        if a == 0:
            return b
        return Rational._gcd(self,b%a, a)

    @property
    #This is called ann @property decorator, used to define read only functions
    def numer(self):
        '''Return the numerator of a rational number.'''
        return(self.numerator)

    @property
    def denom(self):
        '''Return the denominator of a rational number.'''
        return(self.denominator)

    def __str__(self):
        '''Return the string representation of a rational number.'''
        return '{}/{}'.format(self.numerator,self.denominator)

    def __repr__(self):
        '''Return the detailed string representation of a rational number.'''
        return 'rational.Rational({}, {})'.format(self.numerator,self.denominator)

    def __float__(self):
        '''Return the float equivalent of self.'''
        return float(self.numerator/self.denominator)

    def __eq__(self, other):
        '''Return True if self == other, False otherwise.'''
        #checking for equality between two rational numbers by multiplying the denominators to better compare
        inequality1 = self.numerator * other.denominator
        inequality2 = other.numerator * self.denominator
        if inequality1 == inequality2:
            return True
        else:
            return False

    def __ne__(self, other):
        '''Return False if self == other, True otherwise.'''
        inequality1 = self.numerator * other.denominator
        inequality2 = other.numerator * self.denominator
        if inequality1 == inequality2:
            return False
        else:
            return True

    def __lt__(self, other):
        '''Return true if self < other, False otherwise.'''
        inequality1 = self.numerator * other.denominator
        inequality2 = other.numerator * self.denominator
        if inequality1 < inequality2:
            return True
        else:
            return False

    def __le__(self, other):
        ''' Return true if self <= other, False otherwise.'''
        inequality1 = self.numerator * other.denominator
        inequality2 = other.numerator * self.denominator
        if inequality1 <= inequality2:
            return True
        else:
            return False

    def __gt__(self, other):
        ''' Return true if self > other, False otherwise.'''
        inequality1 = self.numerator * other.denominator
        inequality2 = other.numerator * self.denominator
        if inequality1 > inequality2:
            return True
        else:
            return False

    def __ge__(self, other):
        '''Return true if self >= other, False otherwise.'''
        inequality1 = self.numerator * other.denominator
        inequality2 = other.numerator * self.denominator
        if inequality1 >= inequality2:
            return True
        else:
            return False

    def __add__(self, other):
        '''Return the sum of two rational numbers.'''
        sum_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        sum_denominator = self.denominator * other.denominator
        return Rational(sum_numerator, sum_denominator)

    def __sub__(self, other):
        '''Return the difference of two rational numbers.'''
        sub_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        sub_denominator = self.denominator * other.denominator
        return Rational(sub_numerator, sub_denominator)

    def __mul__(self, other):
        '''Return the product of two rational numbers.'''
        mul_numerator = self.numerator * other.numerator
        mul_denominator = self.denominator * other.denominator
        return Rational(mul_numerator, mul_denominator)

    def __truediv__(self, other):
        '''Return the quotient of two rational numbers.'''
        div_numerator = self.numerator * other.denominator
        div_denominator = self.denominator * other.numerator
        return Rational(div_numerator, div_denominator)

    def inverse(self):
        '''Return the multiplicative inverse of a rational number.'''
        inverse_numerator = self.denominator
        inverse_denominator = self.numerator
        return Rational(inverse_numerator, inverse_denominator)

#------------------------------------------------------------------------------
# if this is a stand alone module, i.e. not a program to be run, then you can
# stop here. If this is a program to be run under python, then continue.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# definition of function main()
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
