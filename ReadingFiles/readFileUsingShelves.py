import shelve

if __name__=='__main__':
    path='/Users/parveen.a.naaz/Documents/Python/files/mydata.txt'
    shelfFile = shelve.open('mydata')
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats
    print(shelfFile['cats'])
    print(list(shelfFile.keys()))
    print(list(shelfFile.values()))
    shelfFile.close()