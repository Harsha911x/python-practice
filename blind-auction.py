from art import auction_logo 
import os

biddings=[]
new_bid={}

while(1):
    print(auction_logo)
    name=input("What is your name?\n")
    bid=int(input("Enter your bid : "))
    new_bid[name]=bid
    # print(biddings)
    ch=input("\nAre there any other bidders? [y/n]\n")
    os.system('cls')
    if(ch=='n'):
        winner_name="no one"
        winner_bid=0
        for ele in new_bid:
            if(new_bid[ele]>winner_bid):
                winner_name=ele
                winner_bid=new_bid[ele]
        print("The winner is ",winner_name," with a bid of ",winner_bid)
        quit()



    

