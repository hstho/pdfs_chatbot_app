#hello how are you
# write a function to read a pdf file with the relevant packages installed

from PyPDF2 import PdfReader
import PyPDF2
def get_pdf_text(pdf):
    text = ""
    # print page number
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        try:
            print(page.extract_text())
            text += page.extract_text()
        except:
            pass

    return text


def get_page_numbers(pdf_path):
    page_numbers = []

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_number in range(len(pdf_reader.pages)):
            # PyPDF2 page numbers start from 0
            page_numbers.append(page_number + 1)

    return page_numbers

pdf_file = "/Users/hupsengtho/Desktop/2024-02-05-Macquarie Research-Singapore Banks-106340520.pdf"
page = get_page_numbers("/Users/hupsengtho/Desktop/2024-02-05-Macquarie Research-Singapore Banks-106340520.pdf")
print (page)
text = get_pdf_text(pdf_file)
print (text)