import xlwt
import xlrd
import random
import re

#Open the workbook
book = xlrd.open_workbook('excel.xls')

#Access the first sheet
sheet = book.sheet_by_index(0)

output = open("test.S", "w+")

output.write(".global start \n \n")
output.write("start: \n")
#Iterate through the rows and print the values
#for i in range(1,sheet.nrows):
#print(sheet.cell_value(i,0))
#x = 0
reg="x"+"0"
#print("li",reg," ",0)
output.write("\t"+"li"+" "+reg+" "+"0"+"\n")

def cell_to_reg_list (sheet_cell_row, sheet_cell_col):      #func to extract reg x value from xls cell
    reg = sheet.cell_value(sheet_cell_row,sheet_cell_col)
    y = reg.replace(" ","")      #remove space if user has entered space in the middle of the string
    x = re.split(",",y)         #split string where , is found
    #print(x)
    reg_list = []
    for i in x:
        if re.search("-",i):
            temp = i.replace("x","")
            temp = re.split("-",temp)
            temp_list = ["x" + str(j) for j in range(int(temp[0]),int(temp[1])+1)]
            reg_list += temp_list
        else:
            reg_list.append(i)
    #print(reg_list)
    reg_list = list(set(reg_list))    #unique list

    #print(reg_list)
    return reg_list

def list_subset(set1,set2):
    if(set(set2).issubset(set(set1))):
        pass
    else:
        print("register set mismatch: entered in xls for instruction type is not valid")
        print("superset entered ",set1)
        print("subset entered ",set2)
        print("please enter valid register set")
        exit()



#step-1     source and dest regs
rd_lev1 = cell_to_reg_list(2,1)
rs1_lev1 = cell_to_reg_list(3,1)
rs2_lev1 = cell_to_reg_list(4,1)

#step-2     regs for diff type of instrs
if sheet.cell_value(0,3) == "R-type":
    R_rd_lev2 = cell_to_reg_list(2,4)
    R_rs1_lev2 = cell_to_reg_list(3,4)
    R_rs2_lev2 = cell_to_reg_list(4,4)

list_subset(rd_lev1,R_rd_lev2)
list_subset(rs1_lev1,R_rs1_lev2)
list_subset(rs2_lev1,R_rs2_lev2)

#step-3     regs for each instruction

rd_lev3_dict = {}
rs1_lev3_dict = {}
rs2_lev3_dict = {}

for i in range(1,11):
    rd_lev3 = cell_to_reg_list(i,11)
    rs1_lev3 = cell_to_reg_list(i,12)
    rs2_lev3 = cell_to_reg_list(i,13)

    list_subset(R_rd_lev2,rd_lev3)
    list_subset(R_rs1_lev2,rs1_lev3)
    list_subset(R_rs2_lev2,rs2_lev3)

    instr = sheet.cell_value(i,9) 
    rd_lev3_dict.update({instr:rd_lev3})
    rs1_lev3_dict.update({instr:rs1_lev3})
    rs2_lev3_dict.update({instr:rs2_lev3})
    
    
arthList = []
weightList = []
sampleList = [x for x in range (0,32)]
#print(sampleList)
for i in range(1,sheet.nrows):
    arthList+= [sheet.cell_value(i,9)]
    weightList+= [sheet.cell_value(i,14)]
    ######## checking whether the next entry is valid or not(!white space) ##########
    if sheet.cell_value(i,9) == "":
        break
RAW_reg="x0"

PREV_Dest_reg="x0"
PREV_Source_reg1="x0"
PREV_Source_reg2="x0"

for j in range (0,50):
    instr = random.choices(arthList, weights=weightList, k=1)
    instrType = ""

    for i in range(1,sheet.nrows):
        if(instr[0] == sheet.cell_value(i,9)):
            instrType = sheet.cell_value(i,10)
            break
    #RD = random.choices(rd_lev3_dict[instr[0]])

    RD = random.choices(rd_lev3_dict[instr[0]])
    RS1 = random.choices(rs1_lev3_dict[instr[0]])
    RS2 = random.choices(rs2_lev3_dict[instr[0]])
    
    output.write("\t"+instr[0]+" ") 
    output.write(RD[0] + "," + RS1[0] + "," + RS2[0] + "\n")
            
 
'''
    if(instrType == "R"):
       # randomList = random.choices(sampleList, weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1), k=3)

        rd_lev3_dict

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

'''






