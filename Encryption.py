output=input('Do you want to do Encrypt or Decrypt: ')

if output=='encrypt':
    inp=input("Enter a word to encrypt: ")
    if len(inp)>=3:
        code= inp.replace(inp[0], '')
        code1= code + inp[0]
        code2= 'ngj' + code1 + '154'
        print(f'The encrypted form is {code2}')
    else:
        inp=inp[::-1]
        print(inp)

elif output=='decrypt':
    inp2=input('Enter an encryted word to decrypt: ')
    if len(inp2)<3:
        inp2=inp2[::-1]
    else:
        inp2=inp2[3:-3]
        decode= inp2[-1] + inp2[:-1]
        print(f'The decrypted form is {decode}')

else:
    print('Invalid Input')