from PyPDF2 import PdfFileReader
import os

def rename_pdfs():
    path=input("Please enter your path: ")
    os.chdir(path)
    for filename in os.listdir(path):
        if filename.endswith(".pdf"):
            inputPdf=PdfFileReader(open(filename, "rb"))
            if inputPdf.isEncrypted:
                inputPdf.decrypt('')
            docInfo=inputPdf.getDocumentInfo()
            author=docInfo.author
            title=docInfo.title
            date=docInfo['/CreationDate'][2:6]
            new_name=f'{author}-{date}-{title}.pdf'
            old_file=os.path.join(path, filename)
            new_file=os.path.join(path, new_name)
            os.rename(old_file, new_file)

rename_pdfs()
