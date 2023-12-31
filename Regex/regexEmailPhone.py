import re
if __name__=='__main__':
    phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    #(\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

    emailRegex = re.compile( r'''(
    [a-zA-Z0-9._%+-]+       # username
     @.                     # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    #(\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)
text = str('''800-420-7240
                415-863-9900
                415-863-9950
                info@nostarch.com
                media@nostarch.com
                academic@nostarch.com
                info@nostarch.com''')
matches=[]
for groups in phoneRegex.findall(text):
       #print(groups[5])
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       #if groups[8] != '':
           #phoneNum += ' x' + groups[8]
       #print(phoneNum)
       matches.append(phoneNum)
for groups in emailRegex.findall(text):
       #print(groups)
       matches.append(groups)
print(matches)
# Copy results to the clipboard.
if len(matches) > 0:
    str='\n'.join(matches)
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
