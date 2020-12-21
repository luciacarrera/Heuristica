file1 = open("problema.prob","r+")  
  
print ("Output of Read function is ")
observations ={}
while True:
    # read a single line
    line = file1.readline()
    if not line:
        break
    content=line.split(":")
    if(content[0]=="OBS"):
        obPos = content[1].split(";")
        for ob in obPos:
            print(ob)
    #if(content[0]=="SAT1"):

    
    print(line)
file1.close()

