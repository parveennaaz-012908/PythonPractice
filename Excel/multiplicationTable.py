import openpyxl
import sys

if __name__=='__main__':

    if len(sys.argv) > 1:
	    n = int(sys.argv[1])
	else:
	    n = 6
    wb=openpyxl.Workbook()
    sheet=wb.active
    
    for i in range():
