import datetime, pyperclip

def myFunc():
    print ("This is the test script ready for PROD.")
    print (datetime.datetime.now())
    print ("\n")
    print ("Contents of clipboard: ")
    print (pyperclip.paste())
