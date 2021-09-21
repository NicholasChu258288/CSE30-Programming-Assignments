#------------------------------------------------------------------------------
#  Nicholas  Chu
#  1790585
#  CSE 30-02 Spring 2021
#  pa4
#  ContinuedFractions.py
#  Evaluate rational numbers associated with (finite) continued fractions.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# import statements
#------------------------------------------------------------------------------
import sys
from decimal import *
from rational import *

#------------------------------------------------------------------------------
# definitions of optional helper functions
#------------------------------------------------------------------------------
def usage():
   sys.stderr.write("Usage: $ python3 ContinuedFractions.py <input file> <output file>")
   exit()
# end

#------------------------------------------------------------------------------
# definitions of required functions, classes etc.
#------------------------------------------------------------------------------
def CF(L):
   # a recursive fucntion that takes an input list, L, and returns a Rational object representing the corresponding
   # continued fraction as a rational number
   num = L.pop(0)
   if len(L) >= 1:
      return Rational(num, 1) + Rational(1, 1) / CF(L)
   if len(L) == 0:
      return Rational(num, 1)



#------------------------------------------------------------------------------
# if this is a stand alone module, i.e. not a program to be run, then you can
# stop here. If this is a program to be run under python, then continue.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# definition of function main()
#------------------------------------------------------------------------------
def main():
    getcontext().prec = 100
    if len(sys.argv) != 3:
        usage()
    #end
    try:
        input_file = open(sys.argv[1])
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        usage()
    output_file = open(sys.argv[2], 'w')
    cont_frac_lines = input_file.readlines()
    for line in cont_frac_lines:
        cont_frac_list = list(map(int, line.split()))
        continued_fraction = CF(cont_frac_list)
        print('', file=output_file)
        print(continued_fraction, file=output_file)
        print(Decimal(continued_fraction.numer) / Decimal(continued_fraction.denom), file=output_file)
    #end

    input_file.close()
    output_file.close()

    #end

#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
if __name__ == '__main__':

    main()

#end