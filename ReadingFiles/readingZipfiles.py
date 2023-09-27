'''
    Python can create and open(or extract) ZIP files using functions  in the zipfile module.
    Reading Zip File: To read the content of the ZIP file, first you must create the zipfile object. It is similar to file object 
                      To create the zipfile object , call the zipfile.ZipFile() function, passing it a string  of the .ZIP file's filename.
    Note: zipfile is module in python and ZipFile() is a function.

'''
import zipfile,os
from pathlib import Path
p=Path.home()
exampleZip=zipfile.ZipFile('spam_backup.zip')
''' A zipfile object has namelist() method that returns a list of strings for all the files  and folders contained in the zipfile.
    These string can be passed to the getinfo() Zipfile method to return a zipinfo object about the particular file .zipinfo objects
    have their own  attribites such as filesize and compress_size  in bytes.
'''
print(exampleZip.namelist())
spamInfo=exampleZip.getinfo('spam_backup/capitalsquiz10.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')


'''
Extracting from ZIP Files:  The extractall()  method for zipfile objects extracts all the files and folders from a zip file into the
current directory.
'''

exampleZip.extractall()
'''
    To create your own compressed ZIP files , you must open the zipfile object in write mode  by  passing 'w' as the 2nd argument.
    When you pass a path  to the write() method  of the zipfile object, Python will compress the file at the path  and add it into the
    ZIP file . It create new zip folder and write the file into this zip folder.
    This code will create a new ZIP file named new.zip that has the compressed contents of spam.txt.
'''
newZipFile = zipfile.ZipFile('ziptest1.zip','w')
print(newZipFile.namelist())
newZipFile.write('ziptest/spam.txt',compress_type=zipfile.ZIP_DEFLATED)
newZipFile.close()
exampleZip.close()
