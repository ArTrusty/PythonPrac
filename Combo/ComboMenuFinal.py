chicken = 5.25
beef = 6.25
tofu = 5.75
total = 0
small = 1.00
medium = 1.75
large = 2.25
smallFr = 1.00
mediumFr = 1.50
largeFr = 2.00
ketchUp = 0.25
finalTotal = 0
many_Fr = 0
order = ["","","",""]
sandW_index = 1
drink_index = 4
fr_index = 7
sauce_index = 9


sandW = raw_input("Type of sandwich?(chicken,tofu,beef).")

if sandW == "chicken":
    many_sandW = int(input("How many chicken sandwiches?"))
    sandW_total = many_sandW * chicken
    print("you want chicken? That will be $5.25 each")
elif sandW == "beef":
    many_sandW = int(input("How many beef sandwiches?"))
    sandW_total = many_sandW * beef
    print("you want beef? That will be $6.25 each")
elif sandW == "tofu":
    many_sandW = int(input("How many tofu sandwiches?"))
    sandW_total = many_sandW * tofu
    print("you want tofu? That will be $5.75 each")
else:
    print("sorry that doesn't look like it's one of the options.")

if many_sandW > 0:
    order[0] = str(many_sandW) + sandW + " sandwich(s)"
    print(order)
bev = raw_input("Would you like a drink?(yes/no)")

if bev == "yes":
    drink = raw_input("what size would you like? (small/medium/large)")
    many_drink = int(input("How many drinks?"))
    if many_drink > 0:
        order[1] = str(many_drink) + drink + " drink(s)"
        print(order)
        if drink == "small":
            drink_total = many_drink * small
        
        elif drink == "medium":
            drink_total = many_drink * medium
        
        elif drink == "large":
            drink_total = many_drink * large
        
        else:
            print("Sorry, that doesn't look like one of the options.")
    else:
        print("hmm, so I guess you don't want a drink?")        
else:
    print("okay, no drink.")
    


mcFr = raw_input("do you want fries with that?")

if mcFr == "yes":
    frChoice = raw_input("what size would you like? (small/medium/large)")
    many_Fr = int(input("How many fries?"))
    if many_Fr > 0:
        order[2] = str(many_Fr) + frChoice + " fry(s)"
        print(order)
        if frChoice == "small":
            megaFr = raw_input("would you like to mega size that?")
            if megaFr == "yes":
                fr_Total = many_Fr * largeFr

            
            elif megaFr == "no":
                fr_Total = many_Fr * smallFr
            
            else:
                print("sorry that doesn't look like an option")
        elif frChoice == "medium":
            fr_Total = many_Fr * mediumFr
        
        
        elif frChoice == "large":
            fr_Total = many_Fr * largeFr
        
        
        else:
            print("sorry that doesn't look like an option")
    else:
        print("so, you're not getting fries?")
elif mcFr == "no":
    print("okay, no fries")
else:
    print("sorry that doesn't look like an option")


    
sauceCh = int(input("how many ketchup packets do you want?"))
if sauceCh > 0:
    order[3] = str(sauceCh) + "ketchup(s)"
else:
    print("so no ketchup?")
    
sauceCash = ketchUp * sauceCh 
print("by the way, sauce cost money. That will be:", sauceCash)
    


if mcFr == "yes" and bev == "yes":
    finalTotal = (drink_total + fr_Total + sandW_total + sauceCash) - 1
    print("you get a dollar off discount so your total comes to:", finalTotal)
    print("you bought:", order)
elif mcFr == "no" and bev == "no":
    finalTotal = sandW_total + sauceCash
    print("your total comes to:", finalTotal)
    print("you bought:", order)
elif mcFr == "yes" and bev == "no":
    finalTotal = fr_Total + sandW_total + sauceCash
    print("your total comes to:", finalTotal)
    print("you bought:", order)
elif mcFr == "no" and bev == "yes":
    finalTotal = drink_total + sandW_total + sauceCash
    print("your total comes to:", finalTotal)
    print("you bought:", order)
    
