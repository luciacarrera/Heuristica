f=open("output.txt", "r")
contents =f.read()
content1=contents.split("[{")
content2=content1[1].split("}]")
model=content2[0].split("}, {") #models

mySols={}

CorrectAnswer = True
myInt = 0
for imodel in model:
    solutions=imodel.split(', ')
    solutions.sort() #sort alphabetically
    k=0
    #ALL ANSWERS IN MYSOLS
    for ivar in solutions:
        vars= ivar.split(': ')
        mySols[k]= vars[1]
        k+=1
        #Check Constraint 1
        if vars[1] == '':
            CorrectAnswer = False
    #Check Constraint 2
    if mySols[0]!=mySols[1]:
        CorrectAnswer = False
    #Check Constraint 3
    if mySols[1] == mySols[4] or mySols[1] == mySols[5] or mySols[4] == mySols[5]:
        CorrectAnswer = False
    #Check Constraint 4
    if mySols[5] =="'A12'" and mySols[4]=="'A11'":
        CorrectAnswer = False

    #Check Constraint 5
    if (mySols[3]== "'A7'" and mySols[5]=="'A12") or (mySols[4]== "'A12'" and mySols[5]=="'A7")or (mySols[4]== "'A12'" and mySols[6]=="'A7"):
        CorrectAnswer = False
    print("Model ",myInt," checked.")
    myInt+=1


print("\n Results:", CorrectAnswer)



    

        
        