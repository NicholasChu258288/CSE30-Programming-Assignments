# ------------------------------------------------------------------------------
#  Nicholas  Chu
#  1790585
#  CSE 30-02 Spring 2021
#  pa5
#  TestList.py
#  Test the List type with functions added for pa5
# ------------------------------------------------------------------------------
from list import *

def main():

    #Testing reverse:
    C = List()
    print('Now Testing Reverse:')
    print('List:', C)
    #Testing to see that reverse works even with an empty list
    C.reverse()
    print('Empty list to test reverse:', C) #should just print []
    C.append(1)
    C.reverse()
    print('Testing reverse on 1 element list:', C) #should just print the list
    C.append(2)
    C.append('corn')
    C.append(3)
    C.append('apple')
    print('Before Reverse:',C)
    C.reverse()
    print('Reverse:', C)
    C.reverse()
    print('Reverse(again):', C)
    C.append('apple') #Testing if it reverses properly when there are multiple of the same element
    print('Before Reverse:', C)
    C.reverse()
    print('After Reverse:',C)

    #Testing Remove
    print('')
    print('Now testing remove:')
    C.append('apple')
    print('List before remove:', C)
    C.remove('apple')
    print('List after remove:', C)
    C.append(1)
    C.append('apple')#adding more of the same element to see if it all removes properly and in the desired order
    print('List before remove:', C)
    C.remove('apple')
    print('List after remove:', C)
    C.remove('apple')
    print('List after remove:', C)
    C.remove('apple')
    print('List after remove:', C)
    print('List before remove:', C)
    C.remove(3)
    print('List after remove:', C)
    print('List before remove:', C)
    C.remove(2)
    print('List after remove:', C)
    print('List before remove:', C)
    C.remove(1)
    print('List after remove:', C)
    print('List before remove:', C)
    C.remove('corn')
    print('List after remove:', C)
    print('List before remove:', C)
    C.remove(1)
    print('List after remove:', C)

    #Testing __getitem__:
    print('')
    print('Now testing __getitem__:')
    print('Empty list check:',C[1])
    C.append(1)
    print('List:',C)
    print('Out of range check',C[1])
    print('Data of object:', C[0])
    C.append('potato')
    C.append(2)
    C.append('pear')
    C.append('lion')
    C.append(3)
    print('List with appeneded objects:',C)
    print('Data of object:', C[0])
    print('Data of object:', C[3])
    print('Data of object:', C[1])
    print('Data of object:', C[4])
    print('Data of object:', C[5])
    print('')

    #Now testing __setitem__:
    print('Now testing __setitem__:')
    print('List:',C)
    C[2] = 4
    print('After replacement:',C)
    C[1] = 3
    print('After replacement:', C)
    C[4] = 6
    print('After replacement:', C)
    C[1] = 'tiger'
    print('After replacement:', C)
    C[5] = 'monkey'
    print('After replacement:', C)
    C[0] = 'whale'
    print('After replacement:', C)
    D = List()
    print('Empty list:', D)
    D[1] = 5 #Testing for errors, does work properly
    print('After trying to use __setitem__:', D)
    D.append(5)
    print('Before replacement:', D) #Testing list with singular element
    D[0] = 'apple'
    print('Testing replacing from singular list:',D)
    print('')

    #Testing add
    print('Testing __add__:')
    D.append('zebra')
    E = List()
    print('List1:', C)
    print('List2:', D)
    print('List 3:', E)
    print('List1 + List2:', C + D)
    print('List2 + List1:', D + C)
    print('List3 + List1', E + C)
    print('List1 + List3', C + E)
    print('')

    #Testing __iadd__:
    print(' #Testing __iadd__:')
    print('Adding:', E, 'and', E) #Testing adding empty lists
    E += E
    print('Result:', E)
    print('Adding:', C, 'and', E)
    C += E
    print('Result',C)
    print('Adding:', C, 'and', D)
    C += D
    print('Result', C)
    print('Adding:', C, 'and', C)
    C += C
    print('Result', C)
    print('')


    #Testing __mul__:
    print('Testing __mul__:')
    C.clear()
    C.append(1)
    C.append(2)
    C.append(3)
    C.append(4)
    C.append(5)
    print('List:', C)
    print('List x0:',C*0)
    print('List x1:',C*1)
    print('List x2:',C*2)
    print('List x3:',C*3)
    print('')

    #Testing __rmul__:
    print('Testing __rmul__:')
    print('List:', C)
    print('List x0:',C*0)
    print('List x1:',C*1)
    print('List x2:',C*2)
    print('List x3:',C*3)
# end

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()

# end