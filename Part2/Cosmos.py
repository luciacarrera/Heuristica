#!/usr/bin/env python
# coding=utf-8

# Authors: Lucía Carrera & Manya Khanna
# Version: 4.8
# Since: 15/12/2020

# Libraries
import sys
import os
import os.path

#This class represents the information about the satelites
class satellite:
    def __init__(self, number, measure, downlink, turn, charge, battery):
        self.number= number
        self.measure = measure
        self.downlink = downlink
        self.turn = turn
        self.charge = charge
        self.battery = battery

# This class represents a node
class Node:
    # Initialize the class
    def __init__(self, position:(), parent:()):
        self.position = position
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.t = 0 # Total time
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

# A* search
def astar_search(map, hour, start, end):
    
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node
    open.append(start_node)
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            #path.append(start) 
            # Return reversed path
            return path[::-1]
        # Unzip the current node position
        (x, y) = current_node.position
        # Get neighbors
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        # Loop neighbors
        for next in neighbors:
            # Get value from map
            map_value = map.get(next)
            # Check if the node is a wall
            if(map_value == '#'):
                continue
            # Create a neighbor node
            neighbor = Node(next, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            # Generate heuristics (Manhattan distance)
            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(neighbor.position[1] - start_node.position[1])
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None
# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True
    
def main():
    #first we read input file
    file1 = open("ejemplos\problema.prob","r+")  
    observations ={}
    satelites={}

    while True:
        # read a single line
        line = file1.readline()
        if not line:
            break
        content=line.split(":")
        if(content[0]=="OBS"):
            obPos = content[1].split(";")
            i=0
            for ob in obPos:
                ob = ob.replace("(","")
                ob = ob.replace(")","")
                intOb = ob.split(",")
                for j in range(0, len(intOb)): 
                    intOb[j] = int(intOb[j]) 
                observations[i]=intOb
                i+=1
        if("SAT" in content[0]):
            #this program allows up SAT9, SAT10 will be read as SAT1
            numSat = int(content[0][3])
            intSat = content[1].split(";")
            for j in range(0, len(intSat)): 
                intSat[j] = int(intSat[j]) 
            #SATX: measure; downlink; turn; charge; initialBat
            satellite( numSat, intSat[0], intSat[1], intSat[2], intSat[3], intSat[4])

    file1.close()

    #create map
    width = 12
    height = 4
    map={}
    
    for i in range(0,height):
        for j in range(0,width):
            map[(i, j)] = '-'
    
    for i in range(0,len(observations)):
        map[(observations[i][0],observations[i][1])] = 'O'
        
            
    # print the list
    for i in range(0,height):
        print()
        for j in range(0,width):
            print(map[(i,j)],end=" ")

path = astar_search(map, start, end)



if __name__ == "__main__": main()