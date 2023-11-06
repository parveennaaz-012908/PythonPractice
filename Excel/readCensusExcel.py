import openpyxl,pprint

'''
    *   Reads the data from the Excel spreadsheet
    *   Counts the number of census tracts in each county
    *   Counts the total population of each county
    *   Prints the results
code will 
    *   Open and read the cells of an Excel document with the openpyxl module.
    *   Calculate all the tract and population data and store it in a data structure.
    *   Write the data structure to a text file with the .py extension using the pprint module.

'''

if __name__=='__main__':
    print('Opening the worbook')
    wb = openpyxl.load_workbook('PythonPractice/Excel/censuspopdata.xlsx')
    sheet = wb['Population by Census Tract']
    countryData ={}
    '''
        Fill in countyData with each county's population and tracts.
    ''' 
    print('Reading rows...')

    for row in range(2,sheet.max_row+1):
        # Each row in the spreadsheet has data for one census tract.
        state  = sheet['B' + str(row)].value
        county = sheet['C' + str(row)].value
        pop    = sheet['D' + str(row)].value

        # Make sure the key for this state exists.
        countryData.setdefault(state,{})

        # Make sure the key for this county in this state exists.
        countryData[state].setdefault(county,{'tracts':0,'pop':0})

         # Each row represents one census tract, so increment by one.
        countryData[state][county]['tracts'] += 1
        # Increase the county pop by the pop in this census tract.
        countryData[state][county]['pop'] += int(pop)
print('Writing results...')
resultFile = open('census2010.json', 'w')
resultFile.write('allData = ' + pprint.pformat(countryData))
resultFile.close()
print('Done.')