'''
Description: Topological Sort is the linear ordering of a directed graph. A node "A"
which points to another point "B" is set to be a precursor of "B" in the ordering.
Student's Name: Sayuri Monarrez Yesaki
Student's UT EID: sdm3465
Course Name: CS 313E Elements of Software design
Unique Number: 51335
Date Created: 04/25/2018
Date Last Modified: 05/4/2018
'''
class Stack (object):
   def __init__ (self):
      self.stack = []

   # add an item to the top of the stack
   def push (self, item):
      self.stack.append ( item )

   # remove an item from the top of the stack
   def pop (self):
      return self.stack.pop()

   # check what item is on top of the stack without removing it
   def peek (self):
      return self.stack[len(self.stack) - 1]

   # check if a stack is empty
   def isEmpty (self):
      return (len(self.stack) == 0)

   # return the number of elements in the stack
   def size (self):
      return (len(self.stack))

class Vertex (object):
   def __init__ (self, label):
      self.label = label
      self.visited = False

   # determine if a vertex was visited
   def wasVisited (self):
      return self.visited

   # determine the label of the vertex
   def getLabel (self):
      return self.label

   # string representation of the vertex
   def __str__ (self):
      return str (self.label)

class Graph (object):
   def __init__ (self):
      self.Vertices = []
      self.adjMat = []

   # check if a vertex already exists in the graph
   def hasVertex (self, label):
      nVert = len (self.Vertices)
      for i in range (nVert):
         if (label == (self.Vertices[i]).label):
            return True
      return False

   # given a label get the index of a vertex
   def getIndex (self, label):
      nVert = len (self.Vertices)
      for i in range (nVert):
         if ((self.Vertices[i]).label == label):
            return i
      return -1

   # add a Vertex with a given label to the graph
   def addVertex (self, label):
      if not self.hasVertex (label):
         self.Vertices.append (Vertex(label))

         # add a new column in the adjacency matrix for the new Vertex
         nVert = len(self.Vertices)
         for i in range (nVert - 1):
            (self.adjMat[i]).append (0)

         # add a new row for the new Vertex in the adjacency matrix
         newRow = []
         for i in range (nVert):
            newRow.append (0)
         self.adjMat.append (newRow)

   # add weighted directed edge to graph
   def addDirectedEdge (self, start, finish, weight = 1):
      self.adjMat[start][finish] = weight

   # return an unvisited vertex adjacent to vertex v
   def getAdjUnvisitedVertex (self, v):
      nVert = len (self.Vertices)
      for i in range (nVert):
         if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
            return i
      return -1

   # get a list of immediate neighbors that you can go to from a vertex
   # return empty list if there are none
   def getNeighbors (self, vertexLabel):
      neighbors = []
      VertexIdx = self.getIndex(vertexLabel)
      nVert = len(self.Vertices)
      for i in range(nVert):
         if self.adjMat[VertexIdx][i] > 0:
            neighbors.append((self.Vertices[i]).label)
      return neighbors

   # get a copy of the list of vertices
   def getVertices (self):
      listVertices = []
      nVert = len(self.Vertices)
      for i in range(nVert):
         listVertices.append((self.Vertices[i]).label)
      return listVertices

   # determine if a directed graph has a cycle
   def hasCycle(self, other):
      ord_list =[]

      #do topo sort of reversed matrix
      rev_topoSort = other.toposort(ord_list)

      #Do toposort according to rev_topoSort order of idx
      postOrder = self.toposort(rev_topoSort)

      return postOrder

   def toposort_helper(self, v, postOrder):
      theStack = Stack()

      # mark vertex v as visited and push on the stack
      (self.Vertices[v]).visited = True
      theStack.push (v)

      # vist other vertices according to depth
      while (not theStack.isEmpty()):
         # get an adjacent unvisited vertex
         u = self.getAdjUnvisitedVertex (theStack.peek())
         if (u == -1):
            #removes the last item in the list
            u = theStack.pop()
            postOrder.append(u)
         else:
            (self.Vertices[u]).visited = True
            theStack.push(u)

   #return list of vertices after a topological sort
   def toposort (self, ord_list):
      postOrder = []

      if len(ord_list) == 0:
         #dfs topological search of reversed matrix
         for i in range(len(self.Vertices)):
            if not((self.Vertices[i]).visited is True):
               self.toposort_helper(i, postOrder)
               # postOrder = self.toposort_helper(self.Vertices[i], postOrder)
      else:
         for idx in ord_list:
            if not((self.Vertices[idx]).visited is True):
               self.toposort_helper(idx, postOrder)
            else:
               return True

      # the stack is empty let us reset the falgs
      nVert = len (self.Vertices)
      for i in range (nVert):
         (self.Vertices[i]).visited = False

      return postOrder[::-1]

def main():
   # create a Graph object
   cities = Graph()
   rev_cities = Graph()

   # open file for reading
   inFile = open ("topo.txt", "r")

   # read the Vertices
   numVertices = int ((inFile.readline()).strip())

   for i in range (numVertices):
      city = (inFile.readline()).strip()
      cities.addVertex (city)
      rev_cities.addVertex(city)

   # read the edges
   numEdges = int ((inFile.readline()).strip())

   for i in range (numEdges):
      edge = (inFile.readline()).strip()
      edge = edge.split()
      start = cities.getIndex(edge[0])
      finish = cities.getIndex(edge[1])

      cities.addDirectedEdge (start, finish, 1)
      rev_cities.addDirectedEdge(finish, start, 1)

   # close file
   inFile.close()

   #test if a directed graph has a cycle
   result = cities.hasCycle(rev_cities)

   if result is True:
      print("True")
   else:
      s =''
      for i in range(len(result)):
         vertex = str(cities.Vertices[result[i]])
         s += vertex
      print(s)

main()
