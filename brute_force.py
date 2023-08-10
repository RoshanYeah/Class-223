import PyPDF2

filename = input('Path to the file: ').strip()
file1 = open(filename, 'rb')
pdfReader1 = PyPDF2.PdfReader(file1)

tried = 0

if not pdfReader1.is_encrypted:
    print('The file is not password protected! You can successfully open it!')
else:
    wordListFile = open('wordlist.txt', 'r', encoding='utf-8', errors='ignore')
    words = wordListFile.read().lower().split('\n')

    for word in words:
        print('Trying to decode password by:',word)
        result = pdfReader1.decrypt(word)
        if result == 1:
            print('Success! The password is: ' + word)
            break
        elif result == 0:
            tried += 1
            print('Passwords tried: ' + str(tried))
            continue
    
    wordListFile.close()

file1.close()
