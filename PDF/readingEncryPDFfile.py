import PyPDF2

if __name__=="__main__":
    pdfReader = PyPDF2.PdfFileReader(open('PythonPractice/PDF/encrypted.pdf', 'rb'))
    print(pdfReader.isEncrypted)
    #pdfReader.getPage(0)## will throw error.
    pdfReader.decrypt('rosebud') #Password pass to open the PDF File
    pageObj = pdfReader.getPage(0)
    print(pageObj)
