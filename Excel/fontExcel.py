import openpyxl
from openpyxl.styles import Font

if __name__=='__main__':
    wb=openpyxl.Workbook()
    sheet=wb['Sheet']
    italic24Font=Font(size=24,italic=True) # Create a font.
    sheet['A1'].font=italic24Font # Apply the font to A1.
    sheet['A1'] = 'Hello, world!'

    fontObj1 = Font(name='Times New Roman', bold=True)
    sheet['B1'].font = fontObj1
    sheet['B1'] = 'Bold Times New Roman'

    fontObj2 = Font(size=24, italic=True)
    sheet['B2'].font = fontObj2
    sheet['B2'] = '24 pt Italic'
    
    wb.save('PythonPractice/Excel/styles.xlsx')
