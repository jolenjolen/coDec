# Created by Jolen Mascarenhas
# When the program asks to provide a path where the message should be stored, please specify full path of either encode.txt or decode.txt  depending on the action you want to perform.
import os
os.system("color f0")
space=' '
choice=input("What would you like to do?\n1) Encrypt    2) Decrypt\n> ")
if choice == '1':
    LETTERSU='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERSL=LETTERSU.lower()
    LETTERS2U='TFOESGHIJKPQCDRXBUVWLAMNYZ'
    LETTERS2L=LETTERS2U.lower()
    OTHERS='1234567890-=_+[}]{;:\'"|\\,<.>/?'
    OTHERS2='1[",3\\2]{;7:49>0-=_+5|6<.\'?8/}'
    message=input("Enter your message > ")
    outpt=""
    a=int()
    for i in message:
        if i in LETTERSU:
            a = LETTERSU.index(i)
            outpt+=LETTERS2U[a]
        if i in LETTERSL:
            a = LETTERSL.index(i)
            outpt+=LETTERS2L[a]
        if i in space:
            outpt+=i
        if i in OTHERS:
            a = OTHERS.index(i)
            outpt+=OTHERS2[a]
    encodepath=input("Enter the full path of the file where you want to store the encrypted message\n> ")    
    f= open(encodepath,"a+")
    f.write(outpt)
    f.write("\n")
    f.close()
    print("\nText successfully encrypted and stored in",encodepath)
    print("\nText Preview > ",outpt)
elif choice == '2':
    LETTERSU='TFOESGHIJKPQCDRXBUVWLAMNYZ'
    LETTERSL=LETTERSU.lower()
    LETTERS2U='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS2L=LETTERS2U.lower()
    OTHERS='1[",3\\2]{;7:49>0-=_+5|6<.\'?8/}'
    OTHERS2='1234567890-=_+[}]{;:\'"|\\,<.>/?'
    message=input("Enter your message > ")
    outpt=""
    a=int()
    for i in message:
        if i in LETTERSU:
            a = LETTERSU.index(i)
            outpt+=LETTERS2U[a]
        if i in LETTERSL:
            a = LETTERSL.index(i)
            outpt+=LETTERS2L[a]
        if i in space:
            outpt+=i
        if i in OTHERS:
            a = OTHERS.index(i)
            outpt+=OTHERS2[a]
    decodepath=input("Enter the full path of the file where you want to store the decrypted message\n> ")      
    f= open(decodepath,"a+")
    f.write(outpt)
    f.write("\n")
    f.close()
    print("\nText successfully decrypted and stored in",decodepath)
    print("\nText Preview > ",outpt)
