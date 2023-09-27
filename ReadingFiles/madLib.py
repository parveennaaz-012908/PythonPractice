import re
if __name__=='__main__':
    path='/Users/parveen.a.naaz/Documents/Python/files/mydata1.txt'
    madLibFile=open(path,'r')
    content=madLibFile.read()
    madLibFile.close()
    print(content)
    check = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
    #Loop to check for the words to replace
    new_content = content
    matches=check.findall(content)
    for word in matches:
        user_input = input('Enter %s: ' % word)
        new_content = new_content.replace(word,user_input)  # overwrite new_content here
    print(new_content)
    