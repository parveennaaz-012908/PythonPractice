import os, re,shutil

'''
    ! python3
    renameDates.py - Renames filenames with American MM-DD-YYYY date format
    to European DD-MM-YYYY.
'''

if __name__=='__main__':
    '''
    create regext that matches the filename with the American date.
    '''
    datePattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)
    fileList=os.listdir('renameDir')
    for american_file in fileList:
        #print(filename)
        match1=datePattern.search(american_file)
        print(match1.groups())
        # If file not found then don't break out of the loop
        if match1 == None:
            continue

        
        #Grouping the date format
        before_date=match1.group(1)
        monthPart=match1.group(2)
        dayPart=match1.group(4)
        yearPart=match1.group(6)
        afterPart=match1.group(8)

        # European-Style format
        european_file = before_date + dayPart + '-' + monthPart + '-' + yearPart + afterPart
        print(european_file)
    # Get the absolute path of both files
    
        absolute = os.path.abspath('renameDir')
        american_file = os.path.join(absolute,american_file)
        european_file = os.path.join(absolute,european_file)

	# Renaming the file to European-Style format

        shutil.move(american_file,european_file)




