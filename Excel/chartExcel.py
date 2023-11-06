import openpyxl


if __name__=='__main__':
    wb=openpyxl.Workbook()
    sheet=wb.active
    for i in range(1,11):
        sheet['A'+str(i)]=1

    refObj=openpyxl.chart.Reference(sheet,min_col=1,min_row=1, max_col=1,max_row=10)
    seriesObj=openpyxl.chart.Series(refObj,title='First Series')
    chartObj=openpyxl.chart.BarChart()
    chartObj.title='My Chart'
    chartObj.append(seriesObj)
    sheet.add_chart(chartObj,'C5')
    wb.save('PythonPractice/Excel/sampleChart.xlsx')