import pyttsx3 as pt #importing the package of text to speech
import PyPDF2 as pdf #importing the package to open, format and read the pdf file

name= 'part1.pdf' #the user can specify the name of the book to read here

book= open(name, 'rb') #opening the book in binary format
pdfReader= pdf.PdfFileReader(book) #reading the binary format of the book through file reader

pages= pdfReader.numPages #counting the number of pages in the book

friend= pt.init() #initializing the variable

for num in range(0,pages):
 page= pdfReader.getPage(num) #get the page to read
 text= page.extractText() #extracting the text of the page
 friend.say(text) #reciting the content of the text
 friend.runAndWait()

