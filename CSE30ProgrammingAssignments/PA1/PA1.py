def to_string(B):
    #supposed to convert bit list, ex.[*,0,1,0,1] which will be B to elements into a subset so in this case take the set
    #is [1,2,3,4], this will get the positions of all 1's create a list that is [2,4], the * is always the first element
    #as it represents the subset so probably implement something like a for loop that gets the index of each 1 then
    #subtract 1 then used those to create the subset
    bitlist = '{'

    index_position = 0
    for binary_num in B:
        if binary_num == 1:
            bitlist = bitlist + str(index_position) + ','
        index_position += 1
    bitlist = bitlist.rstrip(bitlist[-1]) + '}'

    if len(bitlist) == 0:
        bitlist = '{}'
        return bitlist
    else:
        return bitlist
    #dont know if * will be included, if yes then adjust index pos to either 0 or 1 (zero for if place holder and 1 if
    #there isn't)
    # '*' represents index at zero and is just a placeholder, supposed to be used for grading?

#the first input B is supposed the bit vector to be length of set (n), the second is supposed to be k which is supposed
#to represent number of elements in each subset, i is suppossed to mean element included in subset so moving down a tree
#it checks if that element is in the subset, remember have 0<k<n, supposed to get printSubset running inside of itself

def printSubsets(B,k,i):
    if k != 0 and k+1 == len(B):
        bit_list_if_n_equals_k= ['*']
        for zero in range(0,len(B)-1):
            bit_list_if_n_equals_k.append(1)
        print(to_string(bit_list_if_n_equals_k))
    elif k == 0 or k+1 == len(B):
        print(to_string(B))
    else:
        #if subset will include i
        if k > 0 and i+1 <= len(B):
            B_include_i = B.copy()
            B_include_i.pop(i)
            B_include_i.insert(i,1)
            printSubsets(B_include_i,k-1,i+1)
        #if subset will not include i
        if k-1 >= 0 and i+1 <= len(B):
            B_dont_include_i = B.copy()
            printSubsets(B_dont_include_i,k,i+1)


if __name__ =='__main__':

    import sys
    #using try to make sure that there are two inputs and both are valid, except cause to program to not do anyhting
    try:
        n = int(sys.argv[1])#takes first command line arguement
        k = int(sys.argv[2])#takes second command line arguement
        if n >= k:
            B = []
            B.append('*')
            for bit_list_element in range(0,n):
               B.append(0)
            printSubsets(B,k,1)
    except:
        pass
    #(Personal Note) To test in powershell use:
    #cd Documents
    #cd CSEProgrammingAssignments
    #python

