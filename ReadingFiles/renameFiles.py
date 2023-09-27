import os

'''
The os.walk() function is passed a single string value: the path of the folder.It can be use  os.walk() in a for loop statement to walk 
a directory tree.Unlike the range(), the os.walk() function will return 3 values on each iteration through loop.
    - A string  of the current folder's name.
    - A list of strings of the folders in the current folder.
    - A list of strings of the files in the current folder.
'''
''' 
    Since os.walk() return list of strings for the subfolder  and filename variables, you can use these lists  in their own fors loop
    Replace the print() function calls with your own custom code    

'''

if __name__=='__main__':
    for folderName, subfolders,filenames in os.walk('/Users/parveen.a.naaz/Documents/Python'):
        print('The current folder is '+ folderName)
        for subfolder in subfolders:
            print('SUBFOLDER OF '+ folderName+':'+ subfolder)
        for filename in filenames:
            print('FILE INSIDE '+folderName+':'+folderName)
        print('')