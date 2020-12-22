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
    
class observation:
    def __init__(self, number, measure, downlink, turn, charge, battery):
        self.number= number
        self.measure = measure
        self.downlink = downlink
        self.turn = turn
        self.charge = charge
        self.battery = battery

# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True

#def state(map,)
def main():
    arguments= sys.argv
       
    #first we read input file
    file1 = open(arguments[1],"r+")  
    heuristic = arguments[2]
    observations ={}
    satelites = {1,2}

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
            if numSat == 1:
                sat1 = satellite( numSat, intSat[0], intSat[1], intSat[2], intSat[3], intSat[4])
            elif numSat == 2:
                sat2 = satellite( numSat, intSat[0], intSat[1], intSat[2], intSat[3], intSat[4])
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
        print
        for j in range(0,width):
            print map[(i,j)], " ",

#path = astar_search(map, start, end)



if __name__ == "__main__": main()