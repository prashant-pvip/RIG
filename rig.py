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

if sheet.cell_value(1,7) == 1:
    #randomize
    for i in range(1,32):
        temp = random.randint(0,500)
        reg="x"+str(i)
        #print("li ",reg,",",temp)
        fo.write("\t"+"li"+" "+reg+","+str(temp)+"\n")
else:
    #take value from xls
    for i in range(1,32):
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

for j in range (0,50):
    instrList = random.choices(arthList, weights=weightList, k=1)
    instrType = ""
    for i in range(1,sheet.nrows):
        if(instrList[0] == sheet.cell_value(i,0)):
            instrType = sheet.cell_value(i,2)
            break
    if(instrType == "R"):
            randomList = random.choices(sampleList, weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10,10,10,50,50,50), k=3)
            #print(randomList) 
            #print(instrList[0],end=" ")
            fo.write("\t"+instrList[0]+" ")
            for i in range (0,3):
                regx="x"+str(randomList[i])
                if (i<2):
                    #print(regx,end=",")
                    fo.write(regx+",")
                else:
                    #print(regx)
                    fo.write(regx+"\n")
    if(instrType == "I"):
            randomList = random.choices(sampleList, weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10,10,10,50,50,50), k=2)
            imm = random.randint(0,500)
            #print(randomList) 
            #print(instrList[0],end=" ")
            fo.write("\t"+instrList[0]+" ")
            for i in range (0,3):
                if (i<2):
                    regx="x"+str(randomList[i])
                    #print(regx,end=",")
                    fo.write(regx+",")
                else:
                    #print(regx)
                    fo.write(str(imm)+"\n")
