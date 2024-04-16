import os
import random

os.system('cls')
wordlist=["harshavardhan","japan","government"]
word=random.choice(wordlist)
n=len(word)/2
i=1
ques=list(word)
letterlist=list(word)
while(i<=n):
    x=random.randint(0,len(word)-1)
    ques[x]="_"
    i+=1
ques_str="".join(ques)
life=5
while(life>=0 and "_" in ques):
    print(ques_str)
    print("Remaining life : ",life)
    chr=input("Enter the missing letter : ")
    n=len(letterlist)
    for i in range(n):
        if chr==letterlist[i]:
            ques[i]=chr
        ques_str="".join(ques)
    if chr not in letterlist:
        life-=1
    os.system('cls')
if(ques_str==word):
    print("Congratulations!!!\n****YOU WIN****")
else:
    print("****YOU LOSE****")