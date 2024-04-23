from art import bj_logo 
print(bj_logo)

import random as rd

cards={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"K":10,"Q":10,"J":10,"A":10}

play=int(input("Do you want to play a game of BlackJack? [0/1] : "))

while(play):
    your_cards=[]
    dealer_cards=[]
    your_score=0
    dealer_score=0
    for i in range(2):
        x=rd.choice(list(cards.keys()))
        your_cards.append(x)

    for i in your_cards:
        your_score+=cards[i]

    x=rd.choice(list(cards.keys()))
    dealer_cards.append(x)
    dealer_score+=cards[x]

    print("Your cards are :",your_cards,"\nYour Score = ",your_score,"\n")
    print("Dealer cards are :",dealer_cards,"\nDealer Score = ",dealer_score,"\n")

    deal_play=int(input("Deal? OR Stand? [1/0]"))
    while(deal_play):
        x=rd.choice(list(cards.keys()))
        your_cards.append(x)
        your_score+=cards[x]
        print("Your cards are :",your_cards,"\nYour Score = ",your_score,"\n")
        print("Dealer cards are :",dealer_cards,"\nDealer Score = ",dealer_score,"\n")
        deal_play=int(input("Deal? OR Stand? [1/0]  :  "))

    x=rd.choice(list(cards.keys()))
    dealer_cards.append(x)
    dealer_score+=cards[x]
    print("\nYour cards are :",your_cards,"\nYour Score = ",your_score,"\n")
    print("Dealer cards are :",dealer_cards,"\nDealer Score = ",dealer_score,"\n")

    if(((your_score > dealer_score) and (your_score<21))or(dealer_score>21)):
        print("You WIN!!!")
    else:
        print("You Loose!!!")

    play=int(input("Do you want continue? [0/1] : "))


    #Beautify this and add some money to this
