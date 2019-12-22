#-----------------------------------------------
# Encryption/Decryption Program By Arnold Nunez
#-----------------------------------------------


def main():
    userChoice = displayMenuAndGetOption()
    if userChoice == 'E' or userChoice == 'D':
        fileInput, fileOutput = getFiles(userChoice)
        if fileInput != '' and fileOutput != '':
            convert(fileInput, fileOutput)
    input("\nRun complete. Press the Enter key to exit.")

def displayMenuAndGetOption():
    print('File Encryption Program')
    print()
    print('E = Encrypt a file')
    print('D = Decrypt a file')
    print('Q = Quit the program')
    print()
    userOption = input('Enter menu selection (E, D, or Q): ').upper()
    print()
    if userOption == 'E' or userOption == 'D' or userOption == 'Q':
        return userOption
    else:
        print('Error - Invalid option.')
        print()

def getFiles(userSelection):
    abort = False
    while abort != True:
        if userSelection == 'E':
            fileIn = input('Enter the file to ENCRYPT. Press Enter alone to abort: ')
        elif userSelection == 'D':
            fileIn = input('Enter the file to DECRYPT. Press Enter alone to abort: ')    
        if fileIn != '':
            try:
                fileLoaded = open(fileIn, 'r')
                abort = True
            except IOError:
                print('Error - that file does not exist. Try again.')
                print()
                abort = False
        else:
            abort = True
            fileOut = ''
        if fileIn != '' and abort == True:
                fileOut = input('Enter the output file name: ')
                print()
    return fileIn, fileOut
        
def convert(inputFile, outputFile):
    
    userFile = open(inputFile, 'r')
    fileDataStr = userFile.read()
    userFile.close()

    # Encryption and decryption are inverse of one another
    CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
            'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
            'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
            'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
            'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
            'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
            'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
            'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
            'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
            '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
            '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
            '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
            ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
            "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
            '{':'[','[':'{','}':']',']':'}'}
    
    for ch in fileDataStr:
        value = CODE.get(ch, ch)   
        newFile = open(outputFile, 'a')
        newFile.write(value)
        newFile.close()

#-----------------------------------------------------------------------
# PROGRAM'S MAIN LOGIC
#

main()

