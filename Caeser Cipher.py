import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def encrypt(text,shift):
#     cipher=""
#     for l in text:
#         x=alphabet.index(l)
#         y=x+shift
#         if(y>25):
#             y=y-26
#         new_l=alphabet[y]
#         cipher+=new_l
#     print("encoded messag = "+cipher)
# def decrypt(text,shift):
#     cipher=""
#     for l in text:
#         x=alphabet.index(l)
#         y=x-shift
#         if(y<0):
#             y=26+y
#         new_l=alphabet[y]
#         cipher+=new_l
#     print("decoded messag = "+cipher)
def caeser(text,shift,direction):
    cipher=""
    if(direction=='l'):
        shift*=-1
    for l in text:
        if(l not in alphabet):
            new_l=l
        else:
            x=alphabet.index(l)
            y=x+shift
            new_l=alphabet[y]
        cipher+=new_l
    print("cipher="+cipher)

# op=int(input("Encode-1\nDecode-2\t"))
os.system('cls')
from art import caeser_logo
print(caeser_logo)
q='y'
while(q=='y'):
    text=input("Enter the text\n")
    shift=int(input("Enter the shift\n"))
    if(shift>26):
        shift%=26
    direction=(input("Enter the direction [l/r]\n"))
    caeser(text,shift,direction)
    q=(input("Do you want the continue? [y/n]"))
# if(op==1):
#     encrypt(text,shift)
# else:
#     decrypt(text,shift)
