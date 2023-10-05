
import requests,sys,webbrowser, bs4
'''
        * Gets search keywords from the command line arguments
        * Retrieves the search results page
        * Opens a browser tab for each result
    Code:
        * Read the command line arguments from sys.argv.
        * Fetch the search result page with the requests module.
        * Find the links to each search result. 
        * Call the webbrowser.open() function to open the web browser.
'''

if __name__=='__main__':
    print('Searching.....')
    res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q='+ ' '.join(sys.argv[1:]))
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    # Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.The package-snippet class is used only for search result links
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
#print(numOpen)
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)