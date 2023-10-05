import requests

'''
   - Call requests.get() to download the file.
   - Call open() with 'wb' to create a new file in write binary mode.
   - Loop over the Response object’s iter_content() method.
   - Call write() on each iteration to write the content to the file.
   - Call close() to close the file.
'''
if __name__=='__main__':
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    print(type(res)) # <class 'requests.models.Response'>
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    print(res.status_code == requests.codes.ok) # status of respone so it will print true
    print(len(res.text)) # 178978
    print(res.text[:250]) #  displays only the first 250 characters.
    '''
        This will raise an exception if there was an error downloading the file and will do nothing 
        if the download succeeded.
    '''
    #print(res.raise_for_status()) 

    '''
        you must open the file in write binary mode by passing the string 'wb' as the second argument to open(). 
        Even if the page is in plaintext (such as the Romeo and Juliet text you downloaded earlier), 
        you need to write binary data instead of text data in order to maintain the Unicode encoding of the text.
    '''

    playFile = open('RomeoAndJuliet.txt', 'wb')

    '''
        The iter_content() method returns  "chunks" of the content on each iteration through loop
        Each chunk  is the bytes data type, you get to specify how bytes each chunk will contain
        one hundred thousand bytes is generally good.      
    '''
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
       
    
    
