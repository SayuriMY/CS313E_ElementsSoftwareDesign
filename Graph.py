'''
Description: Graph Traversal
A graph is created from an input file containing information about cities. After
building the initial graph, additional graph manipulation operations will be done.
For example: delete the edge connecting two cities and delete a city.
Student's Name: Sayuri Monarrez Yesaki
Student's UT EID: sdm3465
Course Name: CS 313E Elements of Software design
Unique Number: 51335
Date Created: 04/24/2018
Date Last Modified: 04/24/2018
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

class Queue (object):
   def __init__ (self):
      self.queue = []

   def enqueue (self, item):
      self.queue.append (item)

   def dequeue (self):
      return (self.queue.pop(0))

   def isEmpty (self):
      return (len (self.queue) == 0)

   def size (self):
      return len (self.queue)

   # check what item is on top of the stack without removing it
   def peek (self):
      return self.queue[0]

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

   # add weighted undirected edge to graph
   def addUndirectedEdge (self, start, finish, weight = 1):
      self.adjMat[start][finish] = weight
      self.adjMat[finish][start] = weight

   # return an unvisited vertex adjacent to vertex v
   def getAdjUnvisitedVertex (self, v):
      nVert = len (self.Vertices)
      for i in range (nVert):
         if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
            return i
      return -1

   # do the depth first search in a graph
   def dfs (self, v):
      # create a Stack
      theStack = Stack()

      # mark vertex v as visited and push on the stack
      (self.Vertices[v]).visited = True
      print (self.Vertices [v])
      theStack.push (v)

      # vist other vertices according to depth
      while (not theStack.isEmpty()):
         # get an adjacent unvisited vertex
         u = self.getAdjUnvisitedVertex (theStack.peek())
         if (u == -1):
            #removes the last item in the list
            u = theStack.pop()
         else:
            (self.Vertices[u]).visited = True
            print (self.Vertices[u])
            theStack.push(u)

      # the stack is empty let us reset the falgs
      nVert = len (self.Vertices)
      for i in range (nVert):
         (self.Vertices[i]).visited = False

   # do breadth first search in a graph
   def bfs (self, v):
      # create a Queue
      theQueue = Queue ()

      # make vertex v current and mark it as visited
      current = v
      (self.Vertices[v]).visited = True
      print (self.Vertices [v])
      theQueue.enqueue(v)

      #visit other vertices according to breadth
      while not(theQueue.isEmpty()):
         if theQueue.peek() == v:
            val = theQueue.dequeue()
         # get an adjacent unvisited vertex
         u = self.getAdjUnvisitedVertex (current)
         if (u == -1):
            # remove the first element of the queue and make it current
            current = theQueue.dequeue()
         else:
            # mark the vertex as visited
            (self.Vertices[u]).visited = True
            print(self.Vertices[u])
            # insert vertex into the queue
            theQueue.enqueue(u)

      # the queue is empty let us reset the falgs
      nVert = len (self.Vertices)
      for i in range (nVert):
         (self.Vertices[i]).visited = False

   # get edge weight between two vertices
   # return -1 if edge does not exist
   def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
      FromIdx = self.getIndex(fromVertexLabel)
      ToIdx = self.getIndex(toVertexLabel)
      if (self.adjMat[FromIdx][ToIdx] > 0):
         return self.adjMat[FromIdx][ToIdx]
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

   # delete an edge from the adjacency matrix
   def deleteEdge (self, fromVertexLabel, toVertexLabel):
      weight = self.getEdgeWeight(fromVertexLabel, toVertexLabel)
      if weight != 0 and weight != -1:
         self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)] = 0
      weight2 = self.getEdgeWeight(toVertexLabel, fromVertexLabel)
      if weight2 != 0 and weight2 != -1:
         self.adjMat[self.getIndex(toVertexLabel)][self.getIndex(fromVertexLabel)] = 0

   # delete a vertex from the vertex list and all edges from and
   # to it in the adjacency matrix
   def deleteVertex (self, vertexLabel):
      Idx = self.getIndex(vertexLabel)
      nVer = len(self.Vertices)
      vertex = self.Vertices.pop(Idx)

      # remove column from adj Matrix
      for row in self.adjMat:
            del row[Idx]

      # remove row from adj matrix
      for i in range(nVer):
         if i == Idx:
            del self.adjMat[Idx]

def main():
   # create a Graph object
   cities = Graph()

   # open file for reading
   inFile = open ("graph.txt", "r")

   # read the Vertices
   numVertices = int ((inFile.readline()).strip())
   print (numVertices)

   for i in range (numVertices):
      city = (inFile.readline()).strip()
      print (city)
      cities.addVertex (city)

   # read the edges
   numEdges = int ((inFile.readline()).strip())
   print (numEdges)

   for i in range (numEdges):
      edge = (inFile.readline()).strip()
      print (edge)
      edge = edge.split()
      start = int (edge[0])
      finish = int (edge[1])
      weight = int (edge[2])

      cities.addDirectedEdge (start, finish, weight)

   # print the adjacency matrix
   print ("\nAdjacency Matrix")
   for i in range (numVertices):
      for j in range (numVertices):
         print (cities.adjMat[i][j], end = ' ')
      print ()
   print ()

   # read the starting vertex for dfs and bfs
   startVertex = (inFile.readline()).strip()
   print (startVertex)

   # read cities to delete edge between them
   edge_cities = (inFile.readline()).strip().split()
   print(edge_cities)

   # read city to be deleted
   delVertex = (inFile.readline()).strip()
   print (delVertex)

   # close file
   inFile.close()

   # get the index of the start Vertex
   startIndex = cities.getIndex (startVertex)
   print (startIndex)

   # do depth first search
   print ("\nDepth First Search from " + startVertex)
   cities.dfs (startIndex)
   print()

   # test breadth first search
   print("\nBreadth First Search from " + startVertex)
   cities.bfs(startIndex)
   print()

   #test deletion of an edge
   cities.deleteEdge(edge_cities[0], edge_cities[1])
   print ("\n New Adjacency Matrix")
   numVertices = len(cities.getVertices())
   for i in range (numVertices):
      for j in range (numVertices):
         print (cities.adjMat[i][j], end = ' ')
      print ()
   print ()

   #test deletion of a vertex
   cities.deleteVertex(delVertex)
   print ("\n New Adjacency Matrix")
   numVertices = len(cities.getVertices())
   for i in range (numVertices):
      for j in range (numVertices):
         print (cities.adjMat[i][j], end = ' ')
      print ()
   print ()

   vertices = cities.getVertices()
   print("List of vertices: ")
   print(vertices)
   print()

   #check if it is a connected graph

main()
