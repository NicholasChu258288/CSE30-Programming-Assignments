# ------------------------------------------------------------------------------
#  Nicholas  Chu
#  1790585
#  CSE 30-02 Spring 2021
#  pa3
#  lines.py
#  Definition of the Point and Line classes.
# ------------------------------------------------------------------------------
import math


# ------------------------------------------------------------------------------
#  Do not change the definition of the Point class, other than to define
#  the function join() at the end.
# ------------------------------------------------------------------------------
class Point(object):
    """Class representing a Point in the x-y coordinate plane."""

    def __init__(self, x, y):
        """Initialize a Point object."""
        self.xcoord = x
        self.ycoord = y

    # end

    def __str__(self):
        """Return the string representation of a Point."""
        return '({}, {})'.format(self.xcoord, self.ycoord)

    # end

    def __repr__(self):
        """Return the detailed string representation of a Point."""
        return 'geometry.Point({}, {})'.format(self.xcoord, self.ycoord)

    # end

    def __eq__(self, other):
        """
        Return True if self and other have the same coordinates, False otherwise.
        """
        eqx = (self.xcoord == other.xcoord)
        eqy = (self.ycoord == other.ycoord)
        return eqx and eqy

    # end

    def distance(self, other):
        """Return the distance between self and other."""
        diffx = self.xcoord - other.xcoord
        diffy = self.ycoord - other.ycoord
        return math.sqrt(diffx ** 2 + diffy ** 2)

    # end

    def norm(self):
        """Return the distance from self to the origin (0, 0)."""
        return self.distance(Point(0, 0))

    # end

    def midpoint(self, other):
        """Return the midpoint of the line segment from self to other."""
        midx = (self.xcoord + other.xcoord) / 2
        midy = (self.ycoord + other.ycoord) / 2
        return Point(midx, midy)

    # end

    # ---------------------------------------------------------------------------
    #  Fill in the definition of this function, belonging to the Point class.
    # ---------------------------------------------------------------------------
    def join(self, other):
        """
        If self==other return None. Otherwise return the line passing through
        self and other.
        """

        if self == other:
            return None
        elif self.xcoord == other.xcoord and self.ycoord != other.ycoord:
            return Line(Point(self.xcoord, self.ycoord), 'infinity')
        else:
            if other.xcoord > self.xcoord:
                join_slope = (other.ycoord - self.ycoord) / (other.xcoord - self.xcoord)
            else:
                join_slope = (self.ycoord - other.ycoord) / (self.xcoord - other.xcoord)
            return Line(Point(self.xcoord, self.ycoord), join_slope)
    # end


# end


# ------------------------------------------------------------------------------
#  Fill in the definitions of each method in the Line class.
# ------------------------------------------------------------------------------
class Line(object):
    """Class representing a Line in the x-y coordinate plane."""

    def __init__(self, P, m):
        """Initialize a Line object."""
        self.point = P
        self.slope = m

    # end

    def __str__(self):
        """Return a string representation of a Line."""
        return 'Line through {} of slope {}'.format(self.point, self.slope)

    # end

    def __repr__(self):
        """ Return a detailed string representation of a Line."""
        return 'lines.Line(point={}, slope={})'.format(self.point, self.slope)

    # end

    def __eq__(self, other):
        """
        Return True if self and other are identical Lines, False otherwise.
        """
        if self.contains_point(other.point) == True and self.slope == other.slope:
            return True
        else:
            return False

    # end

    def parallel(self, other):
        """
        Return True if self and other are parallel lines, False otherwise.
        """
        if self.slope == other.slope:
            return True
        else:
            return False

    # end

    def perpendicular(self, other):
        """
        Return True if self and other are perpendicular lines, False otherwise.
        """
        if self.slope == 'infinity' and other.slope == 0:
            return True
        elif self.slope == 0 and other.slope == 'infinity':
            return True
        elif self.slope * other.slope == -1:
            return True
        else:
            return False

    # end

    def contains_point(self, P):
        """
        Return True if self contains point P, False otherwise.
        """
        if self.slope == 'infinity':
            if P.xcoord == self.point.xcoord:
                return True
            else:
                return False
        else:
            b = self.point.ycoord - (self.slope * self.point.xcoord)
            if round(P.ycoord,2) == round(self.slope * P.xcoord + b,2):
                return True
            else:
                return False

    # end

    def intersect(self, other):
        """
        If self and other are parallel, return None.  Otherwise return their
        Point of intersection.
        """
        if self.parallel(other):
            return None
        elif self.slope == 'infinity':
            otherB = other.point.ycoord - (other.slope * other.point.xcoord)
            x_intersect = self.point.xcoord
            y_intersect = other.slope * x_intersect + otherB
            return Point(x_intersect, y_intersect)
        elif other.slope == 'infinity':
            selfB = self.point.ycoord - (self.slope * self.point.xcoord)
            x_intersect = other.point.xcoord
            y_intersect = self.slope * x_intersect + selfB
            return Point(x_intersect, y_intersect)
        else:
            selfB = self.point.ycoord - (self.slope * self.point.xcoord)
            otherB = other.point.ycoord - (other.slope * other.point.xcoord)
            x_intersect = (otherB - selfB) / (self.slope - other.slope)
            y_intersect = self.slope * x_intersect + selfB
            return Point(x_intersect, y_intersect)

    # end

    def parallel_line(self, P):
        """Returns the Line through P that is parallel to self."""
        return Line(P, self.slope)

    # end

    def perpendicular_line(self, P):
        """Returns the Line through P that is perpendicular to self."""
        if self.slope == 'infinity':
            return Line(P, 0)
        elif self.slope == 0:
            return Line(P, 'infinity')
        else:
            perpendicular_slope = -1 / self.slope
            return Line(P, perpendicular_slope)
    # end


# end


# ------------------------------------------------------------------------------
#  Do not change functon main(). Its role is just to test all of the above.
#  Actually you can change it during your own independent testing, but return
#  it to exactly this state before you submit the project.
# ------------------------------------------------------------------------------
def main():
    P = Point(1, 3)
    Q = Point(3, 3)
    R = Point(1, 1)
    S = Point(3, 1)
    T = Point(4, 3)
    U = Point(5, 5)
    V = Point(2, 2)
    W = Point(2, 5)
    X = Point(2, -1)

    A = Line(P, -1)
    B = Line(R, 1)
    C = S.join(T)  # points_to_line(S, T)
    D = Line(W, 'infinity')
    E = Line(Q, 0)
    F = C.parallel_line(P)

    print()
    print('A =', A)
    print(repr(A))
    print()
    print('B =', B)
    print(repr(B))
    print()
    print('C =', C)
    print(repr(C))
    print()
    print('D =', D)
    print(repr(D))
    print()
    print('E =', E)
    print(repr(E))
    print()
    print('F =', F)
    print(repr(F))

    print()
    print(B.intersect(C) == U)
    print(A.intersect(B) == V)
    print(D.intersect(C) == X)
    print(D.intersect(Line(T, 'infinity')) == None)
    print(A.perpendicular(B))
    print(D.perpendicular(E))
    print(A.parallel(B.perpendicular_line(Q)))
    print(A.contains_point(S))
    print(B.contains_point(U))
    print(C.contains_point(X))
    print(F.contains_point(W))

    print()


# end

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()

# end

# ------------------------------------------------------------------------------
#  If your Line class and join() method in the Point class are correct, then
#  the output of function main() should be as follows.
# ------------------------------------------------------------------------------
"""

A = Line through (1, 3) of slope -1
lines.Line(point=(1, 3), slope=-1)

B = Line through (1, 1) of slope 1
lines.Line(point=(1, 1), slope=1)

C = Line through (3, 1) of slope 2.0
lines.Line(point=(3, 1), slope=2.0)

D = Line through (2, 5) of slope infinity
lines.Line(point=(2, 5), slope=infinity)

E = Line through (3, 3) of slope 0
lines.Line(point=(3, 3), slope=0)

F = Line through (1, 3) of slope 2.0
lines.Line(point=(1, 3), slope=2.0)

True
True
True
True
True
True
True
True
True
True
True

"""