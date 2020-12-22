f = open("o.prob","r+")  
  
vars ={}
timeslots={}
while True:
    # read a single line
    line = f.readline()
    if not line:
        break
    
    if line.find("#") == -1:
        #first we split the line into sattelite & time vs. antennaes
        content=line.split(";")

        #we edit the antennaes part so that it is can be legible for the program
        ants = content[1]
        ants = ants.replace("( ",'')
        ants = ants.replace(")","")
        print("ants:",content[0])

        #we add a list of the antennaes that correspond to the sattelite at a certain time
        vars[content[0]] = ants.split(",")

        #now we add the timeslot to our timeslot list so that we can use it our program
        time = content[0].split(":")
        #we must edit the information so that it is properly stored
        time[1] = time[1].replace("( ", "")
        time[1] = time[1].replace(")", "")
        timeslots[content[0]]= time[1].split(",")
        for ob in timeslots[content[0]]:
            print(ob)
        #if(content[0]=="SAT1"):
        #SATX: measure; downlink; turn; charge; initialBat

f.close()

