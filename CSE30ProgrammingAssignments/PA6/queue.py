#------------------------------------------------------------------------------
#  queue.py
#  Definition of the Queue class.
#------------------------------------------------------------------------------

class Queue(object):
   """Queue class implementing FIFO sequence type."""

   def __init__(self):
      """Initialize a Queue object."""
      self._list = []
   # end

   def __str__(self):
      """Return a string representation of self."""
      return str(self._list)
   # end

   def __repr__(self):
      """Return a detailed string representation of self."""
      return repr(self._list)
   # end

   def __len__(self):
      """Return the length of self."""
      return len(self._list)
   # end

   def isEmpty(self):
      """Return true iff self is empty, False otherwise."""
      return (len(self)==0)
   # end

   def enqueue(self, x):
      """Add new item x to back of Queue."""
      self._list.append(x)
   # end

   def dequeue(self):
      """Delete and return front item, or Raise IndexError if empty."""
      if self.isEmpty():
         raise IndexError('dequeue() called on empty Queue')
      else:
         return self._list.pop(0)
      # end
   # end

   def peek(self):
      """Return (only) front item, or raise IndexError if empty."""
      if self.isEmpty():
         raise IndexError('peek() called on empty Queue')
      else:
         return self._list[0]
      # end
   # end


#------------------------------------------------------------------------------
#  Test the Queue type
#------------------------------------------------------------------------------
def main():

   Q = Queue()
   # print(Q.dequeue())
   Q.enqueue('a')
   Q.enqueue('b')
   Q.enqueue('c')
   print(Q.isEmpty())
   print(len(Q))
   print(Q.peek())
   print(Q.dequeue())
   print(Q.dequeue())
   print(Q.dequeue())
   print(Q.isEmpty())
   # Q.dequeue()
   # Q.peek()

# end

#------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end