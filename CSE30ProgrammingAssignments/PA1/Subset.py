#------------------------------------------------------------------------------
#  Nicholas  Chu
#  1790585
#  CSE 30-02 Spring 2021
#  lab2
#  Subset.py
#  Find all possible subsets given n and k, this time not using bitlists to
#  represent each subset
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# import statements
#------------------------------------------------------------------------------
import sys

#------------------------------------------------------------------------------
# definitions of optional helper functions
#------------------------------------------------------------------------------
def usage(arg):
    #useage is a helper function the writes all error messages to stdder
    for element in arg:
        try:
            assert(int(element))
        except ValueError:
            print('cannot parse \'{}\' as int'.format(element), file=sys.stderr)
    print('Usage: python3 Subset.py n k (where 0<=k<=n)', file=sys.stderr)

    #end

#------------------------------------------------------------------------------
# definitions of required functions, classes etc..
#------------------------------------------------------------------------------
def to_string(L):
    """
     Returns the string representation of the subset of {1, 2, ..., n}
     encoded by the list L.
     """
    if len(L) != 0:
        set_string = str(set(L))
        return set_string
    else:
        return '{ }'

    #end

def printSubsets(L,n,k,i):
    if k != 0 and k == n:
        #This is to checkfor a special case if n and k are equal
        list_if_n_equals_k = []
        subset_element = 0
        for element in range(0,n):
            list_if_n_equals_k.append(subset_element)
            subset_element += 1
        print(to_string(list_if_n_equals_k))

    elif k == 0 or k+1 == n:
        print(to_string(L))

    else:
        #if subset will include i
        if k > 0 and i <= n:
            B_include_i = L.copy()
            B_include_i.append(i)
            printSubsets(B_include_i,n,k-1,i+1)
        #if subset will not include i
        if k-1 >= 0 and i <= n:
            B_dont_include_i = L.copy()
            printSubsets(B_dont_include_i,n,k,i+1)

    #end

#------------------------------------------------------------------------------
# if this is a stand alone module, i.e. not a program to be run, then you can
# stop here. If this is a program to be run under python, then continue.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# definition of function main()
#------------------------------------------------------------------------------
def main():
    if len(sys.argv) == 3:
        n = sys.argv[1]
        k = sys.argv[2]
        L = []
        arg_list = [n,k]
        try:
            n = int(sys.argv[1])  # takes first command line arguement
            k = int(sys.argv[2])  # takes second command line arguement
            if 0 <= k and k <= n:
                printSubsets(L, n, k, 1)
            else:
                usage(arg_list)
        except ValueError:
            usage(arg_list)
    else:
        #for here check every input to see it it is an int
        arg_list = []
        for arg in sys.argv[1:]:
            arg_list.append(arg)
        usage(arg_list)


# end

#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end