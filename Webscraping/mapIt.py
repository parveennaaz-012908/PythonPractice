import webbrowser, sys,pyperclip

'''
    1.Read the command line arguments from sys.argv.
    2.Read the clipboard contents.
    3.Call the webbrowser.open() function to open the web browser
'''
'''
 #url= 'https://www.google.com/'
webbrowser.open(url) : This function can launch a new browser to specified URL.
    
'''
'''
    address: mapit 870 Valencia St, San Francisco, CA 94110
'''

if __name__=='__main__':
    if len(sys.argv) > 1:
      '''
        The sys.argv  variables stores a list of the program's filename and command line argument.
        Since sys.argv is a list of strings, you can pass it to the join() method, which returns a
        single string value. it eliminate the first item from list.
      '''
      address=' '.join(sys.argv[1:])
      print("address" ,address)
    else:
        # Get address from clipboard.
        address = pyperclip.paste()
    webbrowser.open('https://www.google.com/maps/place/' + address)