from pathlib import Path

if __name__=='__main__':
    p = Path('spam.txt')
    print(p.write_text(' My first File'))
    #print(p.read_text())

    path='/Users/parveen.a.naaz/Documents/Python/files/hello.txt'
    helloFile = open(Path.home() /'Documents/Python/files/' 'hello.txt')
    #print(helloFile)
    # Open the file with read option.
    helloFile = open(path,'r')
    #print(helloFile)
    # Here , the content of the file will be shown.
    helloContent = helloFile.read()
    #print(helloContent)
   
    print(helloFile.readlines())