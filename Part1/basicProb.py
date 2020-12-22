#import constraint library
from constraint import *

#definition of a variable as our program
problem = Problem()

#creation of variables
vars={}
vars['p'] = ["A1", "A2", "A3", "A4"] #Sat 1 from 00:00 - 12:00
vars['q'] = ["A1", "A2", "A3"] #Sat 2 from 00:00 - 12:00
vars['r'] = ["A4", "A6"] #Sat 3 from 06:00 - 12:00
vars['s'] = ["A7", "A9", "A10"] #Sat 3 from 13:00 - 16:00
vars['t'] = ["A8", "A11", "A12"] #Sat 4 from 16:00 - 00:00
vars['u'] = ["A1", "A7", "A12"] #Sat 5 from 06:00 - 13:00
vars['v'] = ["A7", "A9"] #Sat 6 from 06:00 - 13:00
vars['w'] = ["A3", "A4", "A5"] #Sat 6 from 13:00 - 19:00

for ivar in vars:
    problem.addVariable(ivar,vars[ivar])

timeslots={}
#timeslot[var][0] == beginning of time slot
#timeslot[var][1] == ending of time slot
timeslots['p'] = [0, 12] #Before 12
timeslots['q'] = [0, 12] #Before 12
timeslots['r'] = [6, 12] #Before 12
timeslots['s'] = [13, 16] 
timeslots['t'] = [16, 0]
timeslots['u'] = [6, 13] #Before 12
timeslots['v'] = [6, 13] #Before 12
timeslots['w'] = [13, 19]

#Constraint1: All satellites must have a transmission antenna assigned to it in all its time slots
#This constraint does not need to be programmed as the program already knows it must assign one antennae
#to each satelite in each of its timeslots

#Constraint2: Since SAT1 and SAT2 have similar orbits, it is required to assign them the same antenna
problem.addConstraint( lambda x, y: x==y, ('p','q')) 

#Constraint3: Satellites SAT2, SAT4 and SAT5 should have assigned different antennae.
problem.addConstraint( lambda x, y: x!=y, ('q','t'))
problem.addConstraint( lambda x, y: x!=y, ('q','u'))
problem.addConstraint( lambda x, y: x!=y, ('t','u'))

#Constraint4: In case SAT5 communicates with ANT12, then SAT4 can not communicate with ANT11. 
def constraint4( a, b ):
    if a != "A12" or b!="A11":
        return True

problem.addConstraint( constraint4, ('u','t'))

#Constraint5: If, in any solution, ANT7 and ANT12 are used, then both must be assigned to time slots beginning before 12:00 or after
def constraint5 (a,b):
    if (a!="A7" or b!="A12") and (a!="A12" or b!="A7"):
        return True
        
if InSetConstraint(['A7', 'A12']):
    beginBefore={}
    beginAfter={}
    i=0
    j=0
    for ivar in timeslots:
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
    sols= problem.getSolutions()
    print("Number of solutions: ",len(sols) )
    with open('output.txt', 'w') as f:
            f.write(str(sols))