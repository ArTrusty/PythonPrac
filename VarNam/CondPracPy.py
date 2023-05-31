print("the shop will give you a 10% discount if your total is more than $1000")
cookieUnit = 100
customerInfo = input("amount of cookie units:")
amountUnit = int(customerInfo)
total = amountUnit * 100
if total > 1000:
        discount = total * .1
        final = total - discount
        print("Great!You get a discount. Your cost comes to", final)
else:
    if total < 1000 or total == 1000:
       
        print("sorry, no discount. Your cost comes to ", total )
