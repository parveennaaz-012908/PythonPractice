import re
if __name__=='__main__':

    website_str = '''https://www.regextester.com/
                     Identifying patterns of text
                     https://www.bewakoof.com/
                     https://www.stupid.com/
                     Clean up dates in different date formats
                '''
    websiteRegex=re.compile('''
    [a-z]+ # first character
    ://
    ''',re.VERBOSE)
    for groups in websiteRegex.findall(website_str):
        print(groups)

    dateStr ='3/14/2019'
    replaceRegex=re.compile(r'''
    (\d{1})+
    (\s|/|\.)?                        # separator
    (\d{2})                           # first 3 digits
    (\s|/|\.)                         # separator
    (\d{4})   
    ''',re.VERBOSE)
    for groups in replaceRegex.findall(dateStr):
        print(groups)
        newDate= '-'.join([groups[0],groups[2], groups[4]])
        print(newDate)
    replaceRegex.sub(newDate,dateStr)