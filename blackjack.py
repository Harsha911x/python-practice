from art import bj_logo 
print(bj_logo)

import random as rd

cards={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"K":10,"Q":10,"J":10,"A":10}

def cards_score(your_cards,your_score,dealer_cards,dealer_score):
    print("Your cards are :",your_cards,"\nYour Score = ",your_score,"\n")
    print("Dealer cards are :",dealer_cards,"\nDealer Score = ",dealer_score,"\n")

play=int(input("Do you want to play a game of BlackJack? [0/1] : "))
# pocket=int(input("Enter your buy in amount  :  "))

while(play):
    your_cards=[]
    dealer_cards=[]
    your_score=0
    dealer_score=0

    # bet=int(input("Place your bet : "))
    # if(bet>pocket):
    #     print("You do not have enough in your pocket!")
    #     ch=input("Do you want to buy-in more? [y/n] : ")
    #     if(ch=='y'):
    #         quit()
    #     else:
    #         amt=int(input("Enter your buy-in amt : "))

    for i in range(2):
        x=rd.choice(list(cards.keys()))
        your_cards.append(x)

    for i in your_cards:
        your_score+=cards[i]

    x=rd.choice(list(cards.keys()))
    dealer_cards.append(x)
    dealer_score+=cards[x]

    cards_score(your_cards,your_score,dealer_cards,dealer_score)

    deal_play=int(input("Deal? OR Stand? [1/0]"))
    while(deal_play):
        x=rd.choice(list(cards.keys()))
        your_cards.append(x)
        your_score+=cards[x]
        x=rd.choice(list(cards.keys()))
        dealer_cards.append(x)
        dealer_score+=cards[x]
        cards_score(your_cards,your_score,dealer_cards,dealer_score)
        deal_play=int(input("Deal? OR Stand? [1/0]  :  "))

    if(your_score>21):
        print("You Loose!!!")
        play=int(input("Do you want continue? [0/1] : "))
        continue

    x=rd.choice(list(cards.keys()))
    dealer_cards.append(x)
    dealer_score+=cards[x]
    cards_score(your_cards,your_score,dealer_cards,dealer_score)

    if(((your_score > dealer_score) and (your_score<=21))or(dealer_score>21)):
        print("You WIN!!!")
    else:
        print("You Loose!!!")

    play=int(input("Do you want continue? [0/1] : "))


    #Beautify this and add some money to this
