# author: Xavier Collantes
# date: 09/01/2018
# purpose: Taking pyinstaller for a spin for Windows ready executable code.
# Dependancies will hopefully be intact.

import sys, os, requests, random, datetime, pyperclip


outPath = 'book.txt'
randomBook = str(random.randint(100, 9999))
inBook = 'https://www.gutenberg.org/files/' + randomBook + '/' + randomBook + '.txt'

def myFunc():
    print ("This is the Main\n%s\n" % datetime.datetime.now())
    print ("Contents of the clipboard:\n%s\n" %pyperclip.paste())


def getBook(book, path):
    print("Retrieving a book: \n%s" %inBook)
    try:
        res = requests.get(inBook)
        res.raise_for_status()
        print("Status Code: %s" %res.status_code)
    except Exception as e:
        print("Problem getting book: %s" %e)

    
    try:
        f = open(path, 'wb')
        for chunk in res.iter_content():
            f.write(chunk)

        print(open(path, 'r+').readline())

        f.close()
    except IOError as ioe:
        print("Problem finding write file: %s" %ioe)

    
    
    
if __name__=='__main__':
    getBook(inBook, outPath)
    #print (inBook)
