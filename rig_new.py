import xlwt
import xlrd
import random
import re

#Open the workbook
book = xlrd.open_workbook('excel.xls')

#Access the first sheet
sheet = book.sheet_by_index(0)

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
    reg_list = set(reg_list)    #unique list
    print(reg_list)
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
for i in range(1,11):
    rd_lev3 = cell_to_reg_list(i,11)
    rs1_lev3 = cell_to_reg_list(i,12)
    rs2_lev3 = cell_to_reg_list(i,13)

    list_subset(R_rd_lev2,rd_lev3)
    list_subset(R_rs1_lev2,rs1_lev3)
    list_subset(R_rs2_lev2,rs2_lev3)







