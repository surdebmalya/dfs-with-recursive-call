'''
Implement DFS using adjacency list take a directed graph of size n=10, and randomly select
number of edges in the graph varying from 9 to 45. Identify each edge as forward edge, tree
edge, back edge and cross edge.'''

import networkx as nx
import matplotlib.pyplot as plt
import random

graph = {
    'A' : ['B','C','J'],
    'B' : [],
    'C' : ['D'],
    'D' : ['F'],
    'E' : [],
    'F' : ['E','G'],
    'G' : ['I'],
    'H' : ['A'],
    'I' : ['H'],
    'J' : []
}

class node:
    def __init__(self,name):
        self.name=name
        self.color='WHITE'
        self.a='NIL'
        self.d=0
        self.f=0

def IsTreeEdge(u,v):
    global treeEdges
    pair=(u.name,v.name)
    treeEdges+=[pair]

def IsBackEdge(u,v):
    global allEdges
    pair=(u.name,v.name)
    for i in range(len(allEdges)):
        if allEdges[i]==pair:
            return True
    return False

def IsForwardOrCrossEdge(u,v):
    global forwardEdges
    global crossEdges
    if u.d<v.d:
        #It will be a forward edge
        forwardEdges+=[(u.name,v.name)]
    elif u.d>v.d:
        #It will be a cross edge
        crossEdges+=[(u.name,v.name)]

def DFS_VISIT(g,addressOfWorkingNode,adjacencyListAddress):
    global time
    global treeEdges
    global backEdges
    time+=1
    addressOfWorkingNode.d=time
    addressOfWorkingNode.color='GREY'
    for adjacencyNodeIndex in range(len(adjacencyList[adjacencyListAddress])):
        nodeName=adjacencyList[adjacencyListAddress][adjacencyNodeIndex]
        for i in range(len(allVertices)):
            if addressOfNodes[i].name==nodeName:
                index=i
                break
        if addressOfNodes[index].color=='WHITE':
            #It will be a tree edge
            IsTreeEdge(addressOfWorkingNode,addressOfNodes[index])
            addressOfNodes[index].a=addressOfWorkingNode.name
            for j in range(len(allVertices)):
                if allVertices[j]==addressOfNodes[index].name:
                    passingAddress=j
                    break
            DFS_VISIT(g,addressOfNodes[index],passingAddress)
        elif addressOfNodes[index].color=='GREY':
            #May or may not be back edge
            findingIfBackEdge=IsBackEdge(addressOfWorkingNode,addressOfNodes[index])
            if findingIfBackEdge==True:
                backEdges+=[(addressOfWorkingNode.name,addressOfNodes[index].name)]
        elif addressOfNodes[index].color=='BLACK':
            IsForwardOrCrossEdge(addressOfWorkingNode,addressOfNodes[index])
    addressOfWorkingNode.color='BLACK'
    time+=1
    addressOfWorkingNode.f=time

def DFS(g):
    global time
    global addressOfNodes
    for i in range(len(allVertices)):
        tempVertices=node(allVertices[i])
        addressOfNodes+=[tempVertices]
    time=0
    for i in range(len(allVertices)):
        if addressOfNodes[i].color=='WHITE':
            DFS_VISIT(g,addressOfNodes[i],i)

time=0
addressOfNodes=[]
treeEdges=[]
backEdges=[]
forwardEdges=[]
crossEdges=[]
allVertices=[]
adjacencyList=[]
finalTreeEdges=[]
finalBackEdges=[]
allEdges=[]

for key,vertex in graph.items():
    allVertices.append(key)
    adjacencyList.append(vertex)
#Finding all pairs of edges
for i in range(len(allVertices)):
    for j in range(len(adjacencyList[i])):
        pair=(allVertices[i],adjacencyList[i][j])
        allEdges+=[pair]
DFS(graph)
print(" Starting Node: ",allVertices[0])
print(" Tree Edges: ",treeEdges)
print(" Back Edges: ",backEdges)
print(" Forward Edges: ",forwardEdges)
print(" Cross Edges: ",crossEdges)
G=nx.DiGraph()
G.add_edges_from(allEdges)
plt.figure(figsize =(10, 10))
nx.draw_networkx(G, with_label = True, node_color ='green')
plt.show() 
