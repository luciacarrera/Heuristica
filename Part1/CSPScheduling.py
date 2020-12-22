
# coding=utf-8

# Authors: Lucía Carrera & Manya Khanna
# Version: 2.8
# Since: 15/12/2020

#import constraint library
from constraint import *

#definition of a variable as our program
problem = Problem()

#creation of variables
vars={}
vars['SAT1 (0,12)'] = ["ANT1", "ANT2", "ANT3", "ANT4"] #Sat 1 from 00:00 - 12:00
vars['SAT2 (0,12)'] = ["ANT1", "ANT2", "ANT3"] #Sat 2 from 00:00 - 12:00
vars['SAT3 (6,12)'] = ["ANT4", "ANT6"] #Sat 3 from 06:00 - 12:00
vars['SAT3 (13,16)'] = ["ANT7", "ANT9", "ANT10"] #Sat 3 from 13:00 - 16:00
vars['SAT4 (16,0)'] = ["ANT8", "ANT11", "ANT12"] #Sat 4 from 16:00 - 00:00
vars['SAT5 (6,13)'] = ["ANT1", "ANT7", "ANT12"] #Sat 5 from 06:00 - 13:00
vars['SAT6 (9,13)'] = ["ANT7", "ANT9"] #Sat 6 from 06:00 - 13:00
vars['SAT6 (13,19)'] = ["ANT3", "ANT4", "ANT5"] #Sat 6 from 13:00 - 19:00

for ivar in vars:
    problem.addVariable(ivar,vars[ivar])

timeslots={}
#timeslot[var][0] == beginning of time slot
#timeslot[var][1] == ending of time slot
timeslots['SAT1 (0,12)'] = [0, 12] #Before 12
timeslots['SAT2 (0,12)'] = [0, 12] #Before 12
timeslots['SAT3 (6,12)'] = [6, 12] #Before 12
timeslots['SAT3 (13,16)'] = [13, 16] 
timeslots['SAT4 (16,0)'] = [16, 0]
timeslots['SAT5 (6,13)'] = [6, 13] #Before 12
timeslots['SAT6 (9,13)'] = [9, 13] #Before 12
timeslots['SAT6 (13,19)'] = [13, 19]


#Constraint1: All satellites must have a transmission antenna assigned to it in all its time slots

#Constraint2: Since SAT1 and SAT2 have similar orbits, it is required to assign them the same antenna
for i in vars:
    if "SAT1" in i:
        for j in vars:
            if "SAT2" in j:
                problem.addConstraint( lambda x, y: x==y, (i,j))
                
#Constraint3: Satellites SAT2, SAT4 and SAT5 should have assigned different antennae.
for i in vars:
    if "SAT2" in i:
        for j in vars:
            #(SAT2 != SAT4) or (SAT2 != SAT5)
            if "SAT4" in j or "SAT5" in j:
                problem.addConstraint( lambda x, y: x!=y, (i,j))
    if "SAT4" in i:
        for j in vars:
            #SAT4 != SAT5
            if "SAT5" in j:
                problem.addConstraint( lambda x, y: x!=y, (i,j))
     

#Constraint4: In case SAT5 communicates with ANT12, then SAT4 can not communicate with ANT11. 
def constraint4( a, b ):
    if a != "ANT12" or b!="ANT11":
        return True

for i in vars:
    if "SAT5" in i:
        for j in vars:
            if "SAT4" in j:
                problem.addConstraint(constraint4, (i,j))


#Constraint5: If, in any solution, ANT7 and ANT12 are used, then both must be assigned to time slots beginning before 12:00 or after
def constraint5 (a,b):
    if (a!="ANT7" or b!="ANT12") and (a!="ANT12" or b!="ANT7"):
        return True
        
if InSetConstraint(['ANT7', 'ANT12']):
    beginBefore={}
    beginAfter={}
    i=0
    j=0
    for ivar in timeslots:
        # Time divider == 12
        if timeslots[ivar][0] < 12:
            beginBefore[i]= ivar
            i+=1

        else:
            beginAfter[j]= ivar
            j +=1

    for x in beginBefore:
            for y in beginAfter:
                problem.addConstraint( constraint5, (beginBefore[x],beginAfter[y]))

#Get Solution
#Get Solution
sols= problem.getSolutions()
num=1
print("\nNumber of models: ", len(sols)," \n" )
for i in sols:
    print("Model ",num,": ",i)
    num+=1
