water=1000
milk=1000
coffee=500
profit=0

coffee_list={"e":{
    "cost":1.50,
    "water":100,
    "coffee":20,
    "milk":0
},
"l":{
    "cost":2.50,
    "water":200,
    "coffee":25,
    "milk":150
},
"c":{
    "cost":3.00,
    "water":250,
    "coffee":25,
    "milk":100
}}

def report(c):
    print("\n\n\n")
    print("Milk : ",c["milk"])
    print("Water : ",c["water"])
    print("Coffee : ",c["coffee"])
    print("Cost : ",c["cost"])

def make_order(ord):
    global milk
    global water
    global coffee
    if(milk-ord["milk"]>=0):
        milk=milk-ord["milk"]
    else:
        print("Sorry there is not enough milk.")
        return
    if(water-ord["water"]>=0):
        water=water-ord["water"]
    else:
        print("Sorry there is not enough water.")
        return
    if(coffee-ord["coffee"]>=0):
        coffee=coffee-ord["coffee"]
    else:
        print("Sorry there is not enough coffee.")
        return
    report(ord)

def pay(c):
    print("Please pay $",c["cost"])
    x=float(input("\n"))
    if(x==c["cost"]):
        global profit
        profit=profit+x
        make_order(c)
    else:
        print("Sorry that's not enough money. Money refunded.")
        return

while(1):
    mycoffee=input("\n\n\nWhat would you like? (espresso(e)/latte(l)/cappuccino(c)) : ")

    if(mycoffee=='quit'):
        quit()
    elif(mycoffee=='report'):
        for c in coffee_list:
            report(coffee_list[c])
    else:
        pay(coffee_list[mycoffee])


#Beautify the user experience even more