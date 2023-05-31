person1 = int(input("First person please put your age."))
person2 = int(input("Second person please put your age."))
person3 = int(input("Third person please put your age."))

if person1 > person2 and person1 > person3:
    print("person 1 is the oldest")
elif person2 > person1 and person2 > person3:
    print("person 2 is the oldest")
elif person3 > person1 and person3 > person2:
    print("person 3 is the oldest")
    
if person1 < person2 and person1 < person3:
    print("person 1 is the youngest")
elif person2 < person1 and person2 < person3:
    print("person 2 is the youngest")
elif person3 < person1 and person3 < person2:
    print("person 3 is the youngest")