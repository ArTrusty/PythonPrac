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
sandW = raw_input("Type of sandwich?(chicken,tofu,beef).")
if sandW == 'chicken':
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


bev = raw_input("Would you like a drink?(yes/no)")

if bev == "yes":
    drink = raw_input("what size would you like? (small/medium/large)")
    if drink == "small":
        total = sandW_price + small
        
    elif drink == "medium":
        total = sandW_price + medium
        
    elif drink == "large":
        total = sandW_price + large
        
    else:
        print("Sorry, that doesn't look like one of the options.")
else:
    print("okay, no drink.")
    
mcFr = raw_input("do you want fries with that?")

if mcFr == "yes":
    frChoice = raw_input("what size would you like? (small/medium/large)")
    if frChoice == "small":
        megaFr = raw_input("would you like to mega size that?")
        if megaFr == "yes":
            total2 = total + largeFr
            
        elif megaFr == "no":
            total2 = total + smallFr
            
        else:
            print("sorry that doesn't look like an option")
    elif frChoice == "medium":
        total2 = total + mediumFr
        
        
    elif frChoice == "large":
        total2 = total + largeFr
        
        
    else:
        print("sorry that doesn't look like an option")
        
else:
    print("sorry that doesn't look like an option")
        
sauceCh = float(input("how many ketchup packets do you want?"))
sauceCash = ketchUp * sauceCh 
print("by the way, sauce cost money. That will be:", sauceCash)
    
    

if mcFr == "yes" and bev == "yes":
    finalTotal = (total2 + sauceCash) - 1
    print("you get a dollar off discount so your total comes to:", finalTotal)
    print("you bought:", drink, "drink", sandW, "sandwich", frChoice, "fries")
        
elif mcFr == "no" and bev == "no":
    finalTotal = total2 + sauceCash
    print("your total comes to:", finalTotal)
    print("you bought:",sandW, "sandwich and no fries and no drink")
elif mcFr == "yes" and bev == "no":
    finalTotal = total2 + sauceCash
    print("your total comes to:", finalTotal)
    print("you bought:", sandW, "sandwich", frChoice, "fries but no drink")
elif mcFr == "no" and bev == "yes":
    finalTotal = total2 + sauceCash
    print("your total comes to:", finalTotal)
    print("you bought:", drink, "drink", sandW, "sandwich but no fries")
