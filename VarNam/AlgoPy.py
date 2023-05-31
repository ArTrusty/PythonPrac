
classHave = float(input("How many classes do you have:"))
classAttend = float(input("How many classes have you attended:"))
attendPercent = (classAttend / classHave) * 100
if attendPercent < 75:
    print("You will NOT be allowed to sit in exam because your attendance percentage is:", attendPercent)
else:
    if attendPercent == 75 or attendPercent > 75:
        print("you will be allowed to sit in exam because your attendance percentage is:", attendPercent)

