import os
import sys
from random import *

clauses1 = []
total_length = 0

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, '2sat6.txt')) as file:
	strings = file.readlines()
	total_length = int(strings.pop(0))
	for i in strings:
		clauses1.append(map(int, i.rstrip().split(" ")))

# Python implementation of Kosaraju's algorithm to print all SCCs
 
from collections import defaultdict
  
#This class represents a directed graph using adjacency list representation
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def addEdges(self,big_list):
    	for i in big_list:
    		self.addEdge(-i[0], i[1])
    		self.addEdge(-i[1], i[0])
  
    # A function used by DFS
    def DFSUtil(self,v,visited):
        # Mark the current node as visited and print it
        visited[v]= True
        print v,
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
 
 
    def fillOrder(self,v,visited, stack):
        # Mark the current node as visited 
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
     
 
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
 
  
  
    # The main function that finds and prints all strongly
    # connected components
    def printSCCs(self):
         
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
 
        # Create a reversed graph
        gr = self.getTranspose()
         
        # Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)
 
        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i]==False:
                gr.DFSUtil(i, visited)
                print""

# Create a graph given in the above diagram
g = Graph(total_length * 2)
g.addEdges(clauses1)
g.printSCCs()
#This code is contributed by Neelam Yadav

