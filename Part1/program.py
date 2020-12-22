#import constraint library
from constraint import *

#definition of a variable as our program
problem = Problem()

vars ={}
timeslots={}
vars["SAT1 (0,12)"] = {}
timeslots["SAT1 (0,12)"] = {0,12}
for ivar in vars:
            problem.addVariable(ivar,vars[ivar])


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
                problem.addConstraint( constraint4, (i,j))


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
with open('output.txt', 'w+') as f:
        f.write(str(problem.getSolutions()))
#Get Solution
sols= problem.getSolutions()
print("Number of solutions: ", len(sols) )