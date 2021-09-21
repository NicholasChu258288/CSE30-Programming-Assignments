#------------------------------------------------------------------------------
#  Nicholas  Chu
#  1790585
#  CSE 30-02 Spring 2021
#  pa6
#  graph.py
#  The program is meant to try solve the k-coloring problem
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
class Graph(object):
    """Class representing an undirected graph."""

    def __init__(self, V, E):
        """Initialize a Graph object."""

        # basic attributes
        self._vertices = list(V)
        self._vertices.sort()
        self._edges = list(E)
        self._adj = {x: list() for x in V}

        for e in E:
            x, y = tuple(e)
            self._adj[x].append(y)
            self._adj[y].append(x)
            self._adj[x].sort()
            self._adj[y].sort()
        # end


        # PA 6 Attributes
        # a dictionary whose keys are vertices x, and value _color[x] the color of x
        self._color = {}
        # a dictionary whose keys are vertices x, and value _ecs[x] the excluded color set of x
        self._ecs = {}

        # self added attributes:

        self._allColors = []
        for num in range(len(V)):
            self._allColors.append(num + 1)

        self._colorsUsed = set()

    # end

    @property
    def vertices(self):
        """Return the list of vertices of self."""
        return self._vertices

    # end

    @property
    def edges(self):
        """Return the list of edges of self."""
        return self._edges

    # end

    def __str__(self):
        """Return a string representation of self."""
        s = ''
        for x in self.vertices:
            a = str(self._adj[x])
            s += '{}: {}\n'.format(x, a[1:-1])
        # end
        return s

    # end

    def add_vertex(self, x):
        """Adds a vertex x to self."""
        if x not in self.vertices:
            self.vertices.append(x)
            self.vertices.sort()
            self._adj[x] = list()
        # end

    # end

    def add_edge(self, e):
        """Adds an edge e to self."""
        x, y = tuple(e)
        self.add_vertex(x)
        self.add_vertex(y)
        self._adj[x].append(y)
        self._adj[y].append(x)
        self._adj[x].sort()
        self._adj[y].sort()
        self.edges.append(e)

    # end


    def Color(self):
        '''
        Determine a proper coloring of a graph by assigning a color from the
        set {1, 2, 3, .., n} to each vertex, where n=|V(G)|, and no two adjacent
        vertices have the same color. Try to minimize the number of colors
        used. Return the subset {1, 2, .., k} of {1, 2, 3, .., n} consisting
        of those colors actually used.
        '''
        uncolored_vertices = []

        # setting up color and ecs
        for v in self.vertices:
            self._color[v] = 0
            self._ecs[v] = set()
        # setting up uncolored_vertices

        for vertex in self.vertices:
            uncolored_vertices.append(vertex)

        if len(uncolored_vertices) ==  0:
            return(self._colorsUsed)

        x = uncolored_vertices.pop(0)

        self._color[x] = 1
        for v in self._adj[x]:
            self._ecs[v].update({self._color[x]})

        while len(uncolored_vertices) != 0:  # while uncolored remains unempty
            x = uncolored_vertices.pop(0)
            # this part assigns a color based off its excluded colors, this part seems to be good

            for color in self._allColors:
                if color not in self._ecs[x]:
                    self._color[x] = color
                    self._colorsUsed.update({color})
                    break
                    # end
                # end

            for v in self._adj[x]:
                self._ecs[v].update({self._color[x]})

        return(self._colorsUsed)

    # end

    def getColor(self, x):
        """ Return the color of x."""
        return self._color[x]

    # end

    def _find_best(self, L):
        """Return the index of the best vertex in the list L."""
        #Did not end up using
        pass
    # end


# end



