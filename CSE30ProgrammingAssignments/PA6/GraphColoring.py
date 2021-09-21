#------------------------------------------------------------------------------
#  Nicholas  Chu
#  1790585
#  CSE 30-02 Spring 2021
#  pa6
#  GraphColoring.py
#  The program takes input file that contains number of vertexes and its edges
#  that would represent a graph and shows the minimum number of colors needed to
#  color it and prints it to an output file
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# import statements
#------------------------------------------------------------------------------
from graph import *
import sys

#------------------------------------------------------------------------------
# definitions of optional helper functions
#------------------------------------------------------------------------------
def usage():
   sys.stderr.write("Usage: $ python3 GraphColoring.py <input file> <output file>")
   exit()
# end

#------------------------------------------------------------------------------
# definitions of required functions, classes etc.
#------------------------------------------------------------------------------
def CheckProperColoring(G):
    """
     Return True if no two adjacent vertices in G have like colors,
     False otherwise.
     """
    coloring_proper = True

    for vertex in G._color:
        #print('Vertex',vertex)
        #print('G._color',G._color[vertex])
        #print('G._adj[vertex]', G._adj[vertex])
        for adj_vertex in G._adj[vertex]:
            if G._color[vertex] == G._color[adj_vertex]:
                coloring_proper = False
            #end
        #end
    #end

    return coloring_proper
#end

#------------------------------------------------------------------------------
# definition of function main()
#------------------------------------------------------------------------------
def main():
    # check command line arguments and open files
    input_file = None
    if len(sys.argv) != 3:
        usage()
    # end
    try:
        input_file = open(sys.argv[1])
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        usage()
    # end
    output_file = open(sys.argv[2], 'w')

    # read each line of input file
    number_vertices = input_file.readline()

    # get number of vertices on first line, create vertex list
    number_vertices = number_vertices.split()
    number_vertices = number_vertices[0]
    vertices = []
    for x in range(int(number_vertices)):
        vertices.append(x + 1)

    # create edge list from remaining lines
    edges = []
    for line in input_file:
        edges.append(tuple(int(i) for i in line.split()))
    print(edges)
    # end

    # create graph G
    G = Graph(vertices, edges)

    # Determine a proper coloring of G and print it to the output file
    colors_used = G.Color()
    print(colors_used)
    print(G._ecs)
    print(len(colors_used), 'colors used:', colors_used, file=output_file)
    print('', file=output_file)
    print('vertex    color', file=output_file)
    print('----------------', file=output_file)
    for vertex in G._vertices:
        print(vertex,'         ',int(G.getColor(vertex)),file=output_file)

    input_file.close()
    output_file.close()

    """
    # Check that the coloring is correct
    print(file=outfile)
    msg = 'coloring is proper: {}'.format(CheckProperColoring(G))
    print(msg, file=outfile )
    """

# end

#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()

# end
