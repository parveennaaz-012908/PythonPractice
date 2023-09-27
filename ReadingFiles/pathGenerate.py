from pathlib import Path
import os
if __name__=='__main__':
    myFiles=['accounts.txt', 'details.csv', 'invite.docx']
    for filename in myFiles:
        print(Path(r'C:/Users/parveen.a.naaz',filename))
    print(Path.cwd() ) ## show the current directory of the system.
    print(os.chdir('/Users/parveen.a.naaz/Documents'))
    print(Path.cwd() ) 
    p = Path('C:/Users/Al/spam.txt')
    print(p.parent)
    print(p.name)
    print(p.suffix)
    print(p.drive)
    print(Path.cwd().parents[0])
    print(Path.cwd().parents[1])
    print(Path.cwd().parents[2])
    #print(Path.cwd().parents[3])
    #print(Path.cwd().parents[4])
    #print(Path.cwd().parents[5])
    #print(Path.cwd().parents[6])
    print('/usr/bin'.split(os. sep))
    print(os.path.getsize('/Users/parveen.a.naaz/Documents/Python/jsontocsv.py'))
    print(os.listdir('/Users/parveen.a.naaz/Documents/Python'))

    totalSize=0
    for filename in os.listdir('/Users/parveen.a.naaz/Documents/Python'):
        totalSize=totalSize + os.path.getsize(os.path.join('/Users/parveen.a.naaz/Documents/Python/',filename))
    print(totalSize)
    p1=Path('/Users/parveen.a.naaz/Documents/Python')
    print(list(p1.glob('*')))
    print(list(p1.glob('project?.py')))
    print(list(p1.glob('*.p?')))