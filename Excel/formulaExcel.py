import openpyxl

if __name__=='__main__':
    wb=openpyxl.Workbook()
    sheet=wb.active
    sheet['A1']=200
    sheet['A2']=300
    sheet['A3']='=SUM(A1:A2)' #Set the formula.
    wb.save('PythonPractice/Excel/writeFormula.xlsx')