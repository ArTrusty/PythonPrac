list =[]
max = 0
while max < 10:
    num = int(input("Enter number:"))
    list.append(num)
    max += 1
    print(list)
    
check = int(input("enter another number to see if it is present"))
if check in list:
    print("this number exists in the list")
else:
    print("this number does NOT exist in the list")