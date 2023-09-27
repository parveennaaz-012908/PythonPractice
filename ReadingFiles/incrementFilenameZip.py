import zipfile,os

'''
#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

'''

def backupToZip(folder):
    print('Welcome')
    folder =os.path.abspath('/Users/parveen.a.naaz/Documents/Python/BackUpZipFiles')
    print(folder)
    number=1
    while True:
        zipfilename=os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipfilename):
            break
        number=number+1
        # Create the ZIP file.
        print(f'Creating {zipfilename}...')
        backupZip=zipfile.ZipFile(zipfilename,'w')
        
        for foldername, subfolders, filenames in os.walk(py):
            print(f'Adding files in {foldername}...')
            # Add the current folder to the ZIP file.
            backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue   # don't back up the backup ZIP files
        backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        print('Done')
        

if __name__=='__main__':
    # Walk the entire folder tree and compress the files in each folder.
    backupToZip('Python')
   
    