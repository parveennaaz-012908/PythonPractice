import re
import os

def search(regex,txt):
    searchRegex = re.compile(regex, re.I)
    result = searchRegex.findall(txt)
    print(result)

if __name__=='__main__':

   
    while True:
        dirs = input('Enter the absolute path of the folder that you want to search\n')
        if os.path.exists(dirs) == True:
            print('This folder exists')
            break
    folder = os.listdir(dirs)
    #print(folder)
    user_search = input('Enter the regular expression\n')
    for filename in folder:
        if filename.endswith('.txt'):
            print(os.path.join(dirs,filename))
            txtFile = open(os.path.join(dirs,filename),'r+')
            msg=txtFile.read()
            search(user_search,msg)