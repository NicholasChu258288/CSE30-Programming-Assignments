# ------------------------------------------------------------------------------
#  Nicholas  Chu
#  1790585
#  CSE 30-02 Spring 2021
#  pa5
#  list.py
#  Definition of the List class, emulating Python's list type. Based on a
#  linked list data structure.
# ------------------------------------------------------------------------------

class _Node(object):
    """Private _Node type."""

    def __init__(self, x):
        """Initialize self, a _Node object."""
        self.data = x
        self.next = None
    # end


# end


class List(object):
    """List class emulating Python's list type."""

    def __init__(self, s=None):
        """Initialize self, a List object."""
        self._front = None
        self._back = None
        self._length = 0
        if s:
            for x in s:
                self.append(x)
            # end
        # end

    # end

    def __len__(self):
        """Return the length of self."""
        return self._length

    # end

    def __str__(self):
        """Return a string representation of self."""
        s = '['
        for x in self:
            s += "{}, ".format(repr(x))
        # end
        if len(self) > 0:
            s = s[0:-2] + ']'
        else:
            s += ']'
        # end
        return s

    # end

    def __repr__(self):
        """Return a detailed string representation of self."""
        return 'list.List(' + str(self) + ')'

    # end

    def __iter__(self):
        """Return an iterator over self."""
        N = self._front
        while N:
            yield N.data
            N = N.next
        # end

    # end

    def __eq__(self, other):
        """
        Return True if self and other are the same sequence, False otherwise.
        """
        eq = (len(self) == len(other))
        N = self._front
        M = other._front
        while eq and N:
            eq = (N.data == M.data)
            N = N.next
            M = M.next
        # end
        return eq

    # end

    def append(self, x):
        """Add item x to back of List."""
        N = _Node(x)
        if len(self) == 0:
            self._front = self._back = N
        else:
            self._back.next = N
            self._back = N
        # end
        self._length += 1

    # end

    def clear(self):
        """Delete all items from List."""
        self._front = None
        self._back = None
        self._length = 0

    # end

    def copy(self):
        """Return a (shallow) copy of List."""
        C = List()
        for x in self:
            C.append(x)
        # end
        return C

    # end

    def insert(self, i, x):
        """Add item x at position i of List, where -n<=i<=n and n=len(self)."""
        n = len(self)
        if not isinstance(i, int):
            raise TypeError('insert() index must be integer')
        # end
        if not -n <= i <= n:
            raise IndexError('insert() index out of range')
        # end

        # interpret negative i as position n-|i|
        if i < 0: i += n

        # perform insertion
        N = _Node(x)
        if n == 0:  # sepcial case: insertion into an empty list
            self._front = self._back = N
        elif i == n:  # special case: insertion at the back
            self._back.next = N
            self._back = N
        elif i == 0:  # special case: insertion at the front
            N.next = self._front
            self._front = N
        else:  # general case: 1<=i<=n-1
            P = self._front
            S = P.next
            for j in range(1, i):
                P = S
                S = S.next
            # end
            P.next = N
            N.next = S
        # end
        self._length += 1

    # end

    def pop(self, i=-1):
        """
        Delete item at position i of List, where -n<=i<=(n-1) and n=len(self).
        """
        n = len(self)
        if not isinstance(i, int):
            raise TypeError('pop() index must be integer')
        # end
        if n == 0:
            raise IndexError('cannot pop() empty List')
        # end
        if not -n <= i <= (n - 1):
            raise IndexError('pop() index out of range')
        # end

        # interpret negative i as position n-|i|
        if i < 0: i += n

        # perform deletion
        if n == 1:  # special case: deletion from a 1-element list
            N = self._front
            self._front = self._back = None
        elif i == 0:  # special case: delete front element
            N = self._front
            self._front = N.next
            N.next = None
        else:  # general case: 1<=i<=n-1
            P = self._front
            S = P.next
            for j in range(1, i):
                P = S
                S = S.next
            # end
            N = S
            S = N.next
            P.next = S
            N.next = None
            if not S:  # sub-case: delete back element
                self._back = P
            # end
        # end
        self._length -= 1
        return N.data

    # end

    # ---------------------------------------------------------------------------
    #  Functions to be added to List for pa5
    # ---------------------------------------------------------------------------

    def remove(self, x):
        """
        Delete leftmost occurance of x in List. Raise ValueError if x is not
        contained in self.
        """
        #Setting up variable to be used throughout remove
        in_self = False
        x = _Node(x)

        # First checking for if there is an occurance of x in the list
        N = self._front
        for node in self:
            if x.data == N.data:
                in_self = True
            N = N.next
        #end

        #Rasises a ValueError if x is not contained in self
        if in_self == False:
            raise ValueError
        #end

        #Removes x from list if it exists and does different things depending on lenght of the list
        #No need to code an extra condtion for len(0) becuase that is taken care by in_self
        have_removed = False

        if in_self == True and len(self) == 1:
            self._front = self._back = None
        #end

        if in_self == True and len(self) > 1:
            N = self._front
            P = N.next

            if N.data == x.data:
                #Special case just for when deleting the first element of a list
                self._front = P
                have_removed = True
            #end

            while in_self == True and have_removed == False:
                if P.data == x.data:
                    N.next = P.next
                    P.data = None
                    P.next = None
                    have_removed = True
                else:
                    N = P
                    P = N.next
            #end
        #end
        self._length -= 1
        #end
        return in_self

    # end

    def reverse(self):
        """Reverse the items of List."""
        #Does not need to actually do anything in the cases when the list has a length of 0 or 1
        if len(self) > 1:
            reversed_front = self._back
            reversed_back = self._front

            self._front = reversed_front
            self._back = reversed_back

            N = self._back
            P = N.next
            save_data = N
            N.next = None
            N = P
            while N.next != None:
                P = N.next
                N.next = save_data
                save_data = N
                N = P
            N.next = save_data
        #end

    # end

    def __getitem__(self, i):
        """
        Return item at position i of self, where -n<=i<=n-1 and n=len(self).
        """
        n = len(self)

        #Checking for potential errors
        if not isinstance(i, int):
            raise TypeError('__getitem__ index must be integer')
        if n == 0:
            raise ValueError('list is empty')
        #end
        if not -n <= i <= (n - 1):
            raise ValueError('__getitem__ out of range')
        #end

        #interpret negative i as position n-|i|
        if i < 0: i += n

        #getting item
        N = self._front
        for node in range(i):
            N = N.next
        #end
        #returns item at position i
        return N.data
    # end

    def __setitem__(self, i, x):
        """
        Overwrite item at position i of self by x, where -n<=i<=n-1 and
        n=len(self).
        """
        n = len(self)

        # Checking for potential errors
        if not isinstance(i, int):
            raise TypeError('__setitem__ index must be integer')
        #end
        if n == 0:
            raise ValueError('list is empty')
        # end
        if not -n <= i <= (n - 1):
            raise ValueError('__setitem__ out of range')
        # end

        # interpret negative i as position n-|i|
        if i < 0: i += n

        N = self._front
        x = _Node(x) #need to make x into the node and act as the replacement node

        if n == 1 or n > 1 and i == 0:
            # special case when using __set__ item on beginning element
            N.data = x.data
        else:
            P = N.next
            x.next = P.next
            for node in range(1,i):
                N = P
                P = N.next
                x.next = P.next
            P.data = x.data
            N.next = x
        # end


    # end

    def __add__(self, other):
        """
        Return the concatenation of self with other. This function implements
        the operation self + other.
        """
        #making sure other is an instance of List class
        if not isinstance(other, List):
            raise TypeError('other must be a list')
        #end

        added_list = List()
        for element in self:
            added_list.append(element)
        #end
        for element in other:
            added_list.append(element)
        #end
        return added_list

    # end

    def __iadd__(self, other):
        """
        Replace self by the concatenation of self with other. This function
        implements the operation self += other.
        """
        if not isinstance(other, List):
            raise TypeError('other must be a list')
        #end

        newList = self + other
        self.clear()
        for element in newList:
            self.append(element)
        return self
    # end

    def __mul__(self, n):
        """
        Return the n-fold concatenation of self with self, where n>=0. This
        function implements the operation self*n.
        """
        if not isinstance(n, int):
            raise TypeError('can\'t multiply sequence by non-int of type \'list\'')
        #end
        if not n>=0:
            raise ValueError('n must be greater than or equal to zero')

        mul_list = List()
        #will return empty list when multiplying with 0, thus only needs to do something when n is above 0
        if n > 0:
            #using this to create copy of self
            for element in self:
                mul_list.append(element)
        # end
            for _ in range(1,n):
                mul_list += self
            #end

        return mul_list


    # end

    def __rmul__(self, n):
        """
        Return the n-fold concatenation of self with self, where n>=0, reversing
        the order of self and n. This function implements the operation n*self.
        """
        if not isinstance(n, int):
            raise TypeError('n must be an integer')
        # end
        if not n >= 0:
            raise ValueError('n must be greater than or equal to zero')

        rmul_list = List()
        # will return empty list when multiplying with 0, thus only needs to do something when n is above 0
        if n > 0:
            # using this to create copy of self
            for element in self:
                rmul_list.append(element)
            # end
            for _ in range(1, n):
                rmul_list += self
            # end

        return rmul_list

# end
# ------------------------------------------------------------------------------

