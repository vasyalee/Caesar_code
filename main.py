from functions import *

while True:

    str = input('Enter string\n')
    task = input('Encrypt or decrypt? (e d)\n')
    lang = input('Language? (rus eng)\n')


    if lang == 'eng':
        if task == 'e':
            print(eng_encrypt(str))
        elif task == 'd':
            print(eng_decrypt(str))

    elif lang == 'rus':
        if task == 'e':
            print(rus_encrypt(str))
        elif task == 'd':
            print(rus_decrypt(str))