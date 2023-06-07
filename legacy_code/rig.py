import xlwt
import xlrd
import random

#Open the workbook
book = xlrd.open_workbook('instr.xls')

#Access the first sheet
sheet = book.sheet_by_index(0)

# Open a file
fo = open("test.S", "w+")

fo.write(".global start \n \n")
fo.write("start: \n")
#Iterate through the rows and print the values
#for i in range(1,sheet.nrows):
#print(sheet.cell_value(i,0))
#x = 0
reg="x"+"0"
#print("li",reg," ",0)
fo.write("\t"+"li"+" "+reg+" "+"0"+"\n")


    #randomize
for i in range(1,32):
	if sheet.cell_value(i+1,6) == "":
		temp = random.randint(0,500)
		reg="x"+str(i)
		#print("li ",reg,",",temp)
		fo.write("\t"+"li"+" "+reg+","+str(temp)+"\n")
	else:
    		#take value from xls
    		temp = sheet.cell_value(i+1,6)
    		reg="x"+str(i)
    		#print("li ",reg,",",int(temp))
    		fo.write("\t"+"li"+" "+reg+","+str(int(temp))+"\n")
arthList = []
weightList = []
sampleList = [x for x in range (0,32)]
#print(sampleList)
for i in range(1,sheet.nrows):
    arthList+= [sheet.cell_value(i,0)]
    weightList+= [sheet.cell_value(i,1)]
    ######## checking whether the next entry is valid or not(!white space) ##########
    if sheet.cell_value(i+1,1) == "":
        break
RAW_reg="x0"

PREV_Dest_reg="x0"
PREV_Source_reg1="x0"
PREV_Source_reg2="x0"

for j in range (0,50):
    instrList = random.choices(arthList, weights=weightList, k=1)
    instrType = ""
    RAW=sheet.cell_value(1,10) 
    WAR=sheet.cell_value(2,10)
    WAW=sheet.cell_value(3,10)
    for i in range(1,sheet.nrows):
        if(instrList[0] == sheet.cell_value(i,0)):
            instrType = sheet.cell_value(i,2)
            break

    if RAW and WAR and WAW :
        dependency_randomness=random.randint(1,3)  #0--> no condition    1--> RAW    2--> WAR     3-->WAW
    elif RAW and WAR:
        dependency_randomness=random.randint(1,2)
    elif RAW and WAW:
        dependency_randomness= random.choices([1,3], weights=(1,1), k=1)[0]
    elif WAW and WAR:
        dependency_randomness= random.randint(2,3)
    else:
            dependency_randomness= 1 if RAW else (2 if WAR else 3) 

    if(instrType == "R"):
        randomList = random.choices(sampleList, weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1), k=3)
        #print(randomList) 
        #print(instrList[0],end=" ")

        #print(dependency_randomness)

        RAW_randomness= random.randint(0,4)
        fo.write("\t"+instrList[0]+" ")
        ### code for RAW Hazard
        if(dependency_randomness==1):     ### dependency_randomness==RAW==1 
            if ( RAW_randomness==0 or RAW==0):
                fo.write("x" + str(randomList[0]) + "," + "x" + str(randomList[1]) + "," + "x" + str(randomList[2]) + "\n")
                PREV_Dest_reg = "x" + str(randomList[0])
                PREV_Source_reg1 = "x"+str(randomList[1])
                PREV_Source_reg2 = "x"+str(randomList[2])
            if ( RAW_randomness==1 and RAW==1):
                fo.write("x" + str(randomList[0]) + "," + PREV_Dest_reg + "," + "x" + str(randomList[2]) + "\n")
                PREV_Source_reg1 = PREV_Dest_reg
                PREV_Source_reg2 = "x"+str(randomList[2])
                PREV_Dest_reg = "x" + str(randomList[0])
            if ( RAW_randomness==2 and RAW==1):
                fo.write("x" + str(randomList[0]) + "," + "x" + str(randomList[1]) + "," + PREV_Dest_reg + "\n")
                PREV_Source_reg1 = "x"+str(randomList[1])
                PREV_Source_reg2 = PREV_Dest_reg
                PREV_Dest_reg = "x" + str(randomList[0])
            if ( RAW_randomness==3 and RAW==1):
                fo.write("x" + str(randomList[0]) + "," + PREV_Dest_reg + "," + PREV_Dest_reg + "\n")
                PREV_Source_reg1 = PREV_Dest_reg
                PREV_Source_reg2 = PREV_Dest_reg
                PREV_Dest_reg = "x" + str(randomList[0])
            if ( RAW_randomness==4 and RAW==1):
                fo.write(PREV_Dest_reg + "," + PREV_Dest_reg + "," + PREV_Dest_reg + "\n")
                PREV_Source_reg1 = PREV_Dest_reg
                PREV_Source_reg2 = PREV_Dest_reg
                PREV_Dest_reg = PREV_Dest_reg
            
        
        WAR_randomness = random.randint(0,4)
        if(dependency_randomness==2):     ### dependency_randomness==WAR==2 
            #print("WAR")
            if ( WAR_randomness==0 or WAR==0):
                fo.write("x" + str(randomList[0]) + "," + "x" + str(randomList[1]) + "," + "x" + str(randomList[2]) + "\n")
                PREV_Dest_reg = "x" + str(randomList[0])
                PREV_Source_reg1 = "x"+str(randomList[1])
                PREV_Source_reg2 = "x"+str(randomList[2])
            if ( WAR_randomness==1 and WAR==1):
                fo.write(PREV_Source_reg1 + "," + "x" + str(randomList[1]) + "," + "x" + str(randomList[2]) + "\n")
                PREV_Dest_reg = PREV_Source_reg1
                PREV_Source_reg1 = "x"+str(randomList[1])
                PREV_Source_reg2 = "x"+str(randomList[2])
            if ( WAR_randomness==2 and WAR==1):
                fo.write(PREV_Source_reg2 + "," + "x" + str(randomList[1]) + "," +  "x" + str(randomList[2])+ "\n")
                PREV_Dest_reg = PREV_Source_reg2
                PREV_Source_reg1 = "x"+str(randomList[1])
                PREV_Source_reg2 = "x"+str(randomList[2])            
            if ( WAR_randomness==3 and WAR==1):
                fo.write(PREV_Source_reg1 + "," + PREV_Source_reg1 + "," + PREV_Source_reg1 + "\n")
                PREV_Dest_reg = PREV_Source_reg1
                PREV_Source_reg1 = PREV_Source_reg1
                PREV_Source_reg2 = PREV_Source_reg1 
            if ( WAR_randomness==4 and WAR==1):
                fo.write(PREV_Source_reg2 + "," + PREV_Source_reg2 + "," + PREV_Source_reg2 + "\n")
                PREV_Dest_reg = PREV_Source_reg2
                PREV_Source_reg1 = PREV_Source_reg2
                PREV_Source_reg2 = PREV_Source_reg2 
        

        WAW_randomness= random.randint(0,2)
        if(dependency_randomness==3):     ### dependency_randomness==WAW==3 
            if ( WAW_randomness==0 or RAW==0):
                fo.write("x" + str(randomList[0]) + "," + "x" + str(randomList[1]) + "," + "x" + str(randomList[2]) + "\n")
                PREV_Dest_reg = "x" + str(randomList[0])
                PREV_Source_reg1 = "x"+str(randomList[1])
                PREV_Source_reg2 = "x"+str(randomList[2])
            if ( WAW_randomness==1 and RAW==1):
                fo.write(PREV_Dest_reg + "," +  "x" + str(randomList[1]) + "," + "x" + str(randomList[2]) + "\n")
                PREV_Dest_reg = PREV_Dest_reg 
                PREV_Source_reg1 = "x"+str(randomList[1])
                PREV_Source_reg2 = "x"+str(randomList[2])

            if ( WAW_randomness==2 and RAW==1):
                fo.write(PREV_Dest_reg  + "," + PREV_Dest_reg + "," + PREV_Dest_reg + "\n")
                PREV_Dest_reg =    PREV_Dest_reg
                PREV_Source_reg1 = PREV_Dest_reg
                PREV_Source_reg2 = PREV_Dest_reg

    
    if(instrType == "I"):
        randomList = random.choices(sampleList, weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1), k=2)
        imm = random.randint(0,500)
       

        RAW_randomness= random.randint(0,2)
        fo.write("\t"+instrList[0]+" ")

        if(dependency_randomness==1):     ### dependency_randomness==RAW==1 
            if ( RAW_randomness==0 or RAW==0):
                fo.write("x" + str(randomList[0]) + "," + "x" + str(randomList[1]) + "," + str(imm) + "\n")
                PREV_Dest_reg = "x" + str(randomList[0])
                PREV_Source_reg1 = "x"+str(randomList[1])
            if ( RAW_randomness==1 and RAW==1):
                fo.write("x" + str(randomList[0]) + "," + PREV_Dest_reg + "," + str(imm) + "\n")
                PREV_Source_reg1 = PREV_Dest_reg
                PREV_Dest_reg = "x" + str(randomList[0])
            if ( RAW_randomness==2 and RAW==1):
                fo.write(PREV_Dest_reg + "," + PREV_Dest_reg + "," + str(imm) + "\n")
                PREV_Dest_reg = PREV_Dest_reg
                PREV_Source_reg1 = PREV_Dest_reg
         
        WAR_randomness = random.randint(0,4)
        if(dependency_randomness==2):     ### dependency_randomness==WAR==2 
            if ( WAR_randomness==0 or WAR==0):
                fo.write("x" + str(randomList[0]) + "," + "x" + str(randomList[1]) + "," + str(imm) + "\n")
                PREV_Source_reg1 = "x"+str(randomList[1])
                PREV_Dest_reg = "x" + str(randomList[0])
            if ( WAR_randomness==1 and WAR==1):
                fo.write(PREV_Source_reg1 + "," + "x" + str(randomList[1]) + "," + str(imm) + "\n")
                PREV_Source_reg1 = "x"+str(randomList[1])
                PREV_Dest_reg = PREV_Source_reg1
            if ( WAR_randomness==2 and WAR==1):
                fo.write(PREV_Source_reg2 + "," + "x" + str(randomList[1]) + "," + str(imm)+ "\n")
                PREV_Source_reg2 = "x"+str(randomList[2])            
                PREV_Dest_reg = PREV_Source_reg2
            if ( WAR_randomness==3 and WAR==1):
                fo.write(PREV_Source_reg1 + "," + PREV_Source_reg1 + "," + str(imm) + "\n")
                PREV_Source_reg1 = PREV_Source_reg1
                PREV_Dest_reg = PREV_Source_reg1
            if ( WAR_randomness==4 and WAR==1):
                fo.write(PREV_Source_reg2 + "," + PREV_Source_reg2 + "," + str(imm) + "\n")
                PREV_Source_reg2 = PREV_Source_reg2 
                PREV_Dest_reg = PREV_Source_reg2
        
        WAW_randomness= random.randint(0,2)
        if(dependency_randomness==3):     ### dependency_randomness==WAW==3 
            if ( WAW_randomness==0 or WAW==0):
                fo.write("x" + str(randomList[0]) + "," + "x" + str(randomList[1]) + "," + str(imm) + "\n")
                PREV_Source_reg1 = "x"+str(randomList[1])
                PREV_Dest_reg = "x" + str(randomList[0])
            if ( WAW_randomness==1 and WAW==1):
                fo.write(PREV_Dest_reg + "," +  "x" + str(randomList[1]) + "," + str(imm) + "\n")
                PREV_Source_reg1 = "x"+str(randomList[1])
                PREV_Dest_reg = PREV_Dest_reg 

            if ( WAW_randomness==2 and WAW==1):
                fo.write(PREV_Dest_reg  + "," + PREV_Dest_reg + "," + str(imm) + "\n")
                PREV_Dest_reg =    PREV_Dest_reg
                PREV_Source_reg1 = PREV_Dest_reg

