import xlwt
import xlrd
import random

#Open the workbook
book = xlrd.open_workbook('instr1.xls')

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
for j in range (0,50):
    instrList = random.choices(arthList, weights=weightList, k=1)
    instrType = ""
    RAW=sheet.cell_value(1,10) 
    WAR=sheet.cell_value(2,7)
    WAW=sheet.cell_value(3,7)
    for i in range(1,sheet.nrows):
        if(instrList[0] == sheet.cell_value(i,0)):
            instrType = sheet.cell_value(i,2)
            break
    if(instrType == "R"):
        randomList = random.choices(sampleList, weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1), k=3)
        #print(randomList) 
        #print(instrList[0],end=" ")
        RAW_randomness= random.randint(0,3)
        print(str(RAW_randomness))

        fo.write("\t"+instrList[0]+" ")
        ### code for RAW Hazard
        if ( RAW_randomness==0 or RAW==0):
            fo.write("x" + str(randomList[0]) + "," + "x" + str(randomList[1]) + "," + "x" + str(randomList[2]) + "\n")
        if ( RAW_randomness==1 and RAW==1):
            fo.write("x" + str(randomList[0]) + "," + RAW_reg + "," + "x" + str(randomList[2]) + "\n")
        if ( RAW_randomness==2 and RAW==1):
            fo.write("x" + str(randomList[0]) + "," + "x" + str(randomList[1]) + "," + RAW_reg + "\n")
        if ( RAW_randomness==3 and RAW==1):
            fo.write("x" + str(randomList[0]) + "," + RAW_reg + "," + RAW_reg + "\n")             
        RAW_reg="x"+str(randomList[0])

    if(instrType == "I"):
        randomList = random.choices(sampleList, weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1), k=2)
        imm = random.randint(0,500)
        RAW_randomness= random.randint(0,1)

        #print(randomList) 
        #print(instrList[0],end=" ")
        fo.write("\t"+instrList[0]+" ")
        if ( RAW_randomness==0 or RAW==0):
            fo.write("x" + str(randomList[0]) + "," + "x" + str(randomList[1]) + "," + str(imm) + "\n")
        if ( RAW_randomness==1 and RAW==1):
            fo.write("x" + str(randomList[0]) + "," + RAW_reg + "," + str(imm) + "\n")
            
        RAW_reg="x"+str(randomList[0])
