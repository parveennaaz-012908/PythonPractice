import shutil, os
import send2trash
from pathlib import Path
if __name__=='__main__':
    p=Path.home()
    path='/Users/parveen.a.naaz/Documents/Python/spam_backup'
    # copy the file content into new file.
    #shutil.copy(p / '/Users/parveen.a.naaz/Documents/Python/files/spam.txt', p / '/Users/parveen.a.naaz/Documents/Python/files2')
    # creates new folder 
    #shutil.copytree(p / '/Users/parveen.a.naaz/Documents/Python/files', p / '/Users/parveen.a.naaz/Documents/Python/spam_backup')
    ''' move the file or folder at the path source to the path destination 
    and will return a string of the absolute path of the new location'''
    #shutil.move('/Users/parveen.a.naaz/Documents/Python/files/spam.txt', '/Users/parveen.a.naaz/Documents/Python/spam_backup')
    ''' Permanently deleting files and folders
        You can delete single file or single empty folder with function in the os module, whereas to delete a folder 
        and all it contents, you use the shutil module'''
    #os.unlink(path='/Users/parveen.a.naaz/Documents/Python/spam.txt') # Can delete the file only.
    '''will delete the folder at path. This folder must be empty of any files or folders.'''
    #os.rmdir(path)
    '''will remove the folder at path, and all files and folders it contains will also be deleted.'''
    #shutil.rmtree(path)

    ''' Note: It is good idea to commented out file name using print(), that would be used to deleted.'''

    '''Safe Deletes with the send2trash Module : Python 's built in shutil.rmtree() function  irreversiby  deletes the files and folder 
    it can be dangerous to use. A much better way to delete the files and folder is with  the third party send2trash module.'''


    baconFile= open('bacon.txt','a') #Creates the file.
    baconFile.write('Bacon is not vegetable ')
    baconFile.close()
    send2trash.send2trash('bacon.txt')
    print(os.walk('files'))
