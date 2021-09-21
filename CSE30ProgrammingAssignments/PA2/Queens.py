#------------------------------------------------------------------------------
#  Nicholas  Chu
#  1790585
#  CSE 30-02 Spring 2021
#  pa2
#  Queens.py
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# import statements
#------------------------------------------------------------------------------
import sys

#------------------------------------------------------------------------------
# definitions of optional helper functions
#------------------------------------------------------------------------------

def createBoard(n):
    B = []
    for column in range(n + 1):
        row_list = []
        for row_element in range(n + 1):
            row_list.append(0)
        B.append(row_list)
    return B
# end


def usage():
    print('Usage: python3 Queens.py [-v] number', file=sys.stderr)
    print('Option: -v verbose output, print all solutions', file=sys.stderr)
# end


#------------------------------------------------------------------------------
# definitions of required functions
#------------------------------------------------------------------------------
def placeQueen(B, i, j):
    B[i][j] = 1
    B[i][0] = j
    current_row = i + 1
    left = j - 1
    right = j + 1
    while current_row <= len(B) - 1:
        if left > 0:
            B[current_row][left] = B[current_row][left] - 1
        if right < len(B):
            B[current_row][right] = B[current_row][right] - 1
        B[current_row][j] = B[current_row][j] - 1
        left -= 1
        right += 1
        current_row += 1
# end


def removeQueen(B, i, j):
    B[i][j] = 0
    B[i][0] = 0
    current_row = i + 1
    left = j - 1
    right = j + 1
    while current_row <= len(B) - 1:
        if left > 0:
            B[current_row][left] = B[current_row][left] + 1
        if right < len(B):
            B[current_row][right] = B[current_row][right] + 1
        B[current_row][j] = B[current_row][j] + 1
        left -= 1
        right += 1
        current_row += 1
# end

def findSolutions(B, i, mode):
    # indicaates that solution was found
    accumulated_sum = 0
    if i > len(B)-1:
        if mode == '-v':
            printBoard(B)
        return 1
    else:
        j = 0
        for square in B[i]:
            if square == 0 and j != 0:
                placeQueen(B,i,j)
                accumulated_sum += findSolutions(B,i+1,mode)
                removeQueen(B,i,j)
            j += 1
    return accumulated_sum
# end

def printBoard(B):
    board_queen_indexes = []
    for row in B[1:]:
        board_queen_indexes.append(row[0])
    print(tuple(board_queen_indexes))
# end

#------------------------------------------------------------------------------
# definition of function main()
#------------------------------------------------------------------------------
def main():
        #verbose mode
        if len(sys.argv) == 3 and str(sys.argv[1]) == '-v':
            try:
                mode = str(sys.argv[1])  # takes first command line arguement
                n = int(sys.argv[2])  # takes second command line arguement
                B = createBoard(n)
                print('{}-Queens has {} solutions'.format(n,findSolutions(B,1,mode)))
            except:
                usage()
        elif len(sys.argv) == 2:
            # not verbose mode
            try:
                n = int(sys.argv[1])  # takes first command line arguement
                B = createBoard(n)
                print('{}-Queens has {} solutions'.format(n,findSolutions(B,1,'None')))
            except:
                usage()
        else:
            usage()
# end

#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
if __name__ =='__main__':
    main()