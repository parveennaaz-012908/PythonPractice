import PyPDF2

if __name__=="__main__":
    pdfFileObj = open('PythonPractice/PDF/meetingminutes.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    print(pageObj.extractText())
    pdfFileObj.close()