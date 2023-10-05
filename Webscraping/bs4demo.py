import requests, bs4

if __name__ =='__main__':
    '''
        This code uses requests.get() to download the main page from the No Starch Press website 
        and then passes the text attribute of the response to bs4.BeautifulSoup(). 
        The BeautifulSoup object that it returns is stored in a variable named noStarchSoup.
    '''
    res=requests.get('https://nostarch.com')
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text,'html.parser')
    print(type(noStarchSoup))

    '''
        You can also load an HTML file from your hard drive 
        by passing a File object to bs4.BeautifulSoup() along with a second argument 
        that tells Beautiful Soup which parser to use to analyze the HTML.
    '''
    exampleFile=open('PythonPractice/Webscraping/example.html')
    exampleSoup=bs4.BeautifulSoup(exampleFile,'html.parser')
    print(type(exampleSoup))

    elems = exampleSoup.select('#author')
    print(type(elems))
    print(len(elems))
    print(type(elems[0]))
    print(str(elems[0]))
    print(elems[0].getText())
    print(elems[0].attrs)

    pElems = exampleSoup.select('p')
    print(str(pElems))
    print(pElems[0].getText())
    print(str(pElems[1]))
    print(pElems[1].getText())
    print(str(pElems[2]))
    print(pElems[2].getText())

    spanElem = exampleSoup.select('span')[0]
    print(str(spanElem))
    print(spanElem.get('id'))
    print(spanElem.get('some_nonexistent_addr') == None)
    print(spanElem.attrs)
