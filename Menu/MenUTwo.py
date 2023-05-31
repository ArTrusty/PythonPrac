
chicken = 5.25
beef = 6.25
tofu = 5.75
total = 0
total2 = 0
small = 1.00
medium = 1.75
large = 2.25
smallFr = 1.00
mediumFr = 1.50
largeFr = 2.00
ketchUp = 0.25
finalTotal = 0
sandW = input("Type of sandwich?(chicken,tofu,beef).")
if sandW == "chicken":
    sandW_price = chicken
    print("you want chicken? That will be $5.25")
elif sandW == "beef":
    sandW_price = beef
    print("you want beef? That will be $6.25")
elif sandW == "tofu":
     sandW_price = tofu
     print("you want tofu? That will be $5.75")
else:
    print("sorry that doesn't look like it's one of the options.")


bev = input("Would you like a drink?(yes/no)")

if bev == "yes":
    drink = input("what size would you like? (small/medium/large)")
    if drink == "small drink":
        total = sandW_price + small
        
    elif drink == "medium drink":
        total = sandW_price + medium
        
    elif drink == "large drink":
        total = sandW_price + large
        
    else:
        print("Sorry, that doesn't look like one of the options.")
else:
    print("okay, no drink. Your total so far is:", sandW_price)
    
mcFr = input("do you want fries with that?")

if mcFr == "yes":
    frChoice = input("what size would you like? (small/medium/large)")
    if frChoice == "small fries":
        megaFr = input("would you like to mega size that?")
        if megaFr == "yes":
            total2 = total + largeFr
            
        elif megaFr == "no":
            total2 = total + smallFr
            
        else:
            print("sorry that doesn't look like an option")
    elif frChoice == "medium fries":
        total2 = total + mediumFr
        
        
    elif frChoice == "large fries":
        total2 = total + largeFr
        
        
    else:
        print("sorry that doesn't look like an option")
        
sauceCh = float(input("how many ketchup packets do you want? The max is 10"))
while sauceCh < 10.00:
    sauceCash = ketchUp * sauceCh 
    print("the amount of ketchup comes to", sauceCash)
    

    if mcFr == "yes" and bev == "yes":
        finalTotal = (total2 + sauceCash) - 1
        print("your total comes to:", finalTotal)
        print("you bought:", drink, sandW, frChoice)
        
    elif mcFr == "no" and bev == "no":
        finalTotal = total2 + sauceCash
        print("your total comes to:", finalTotal)
        print("you bought:",sandW)
    elif mcFr == "yes" and bev == "no":
        finalTotal = total2 + sauceCash
        print("your total comes to:", finalTotal)
        print("you bought:", sandW, frChoice)
    elif mcFr == "no" and bev == "yes":
        finalTotal = total2 + sauceCash
        print("your total comes to:", finalTotal)
        print("you bought:", drink, sandW)
        
        
        
        
        
        