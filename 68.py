'''
age = 23

if age >= 18:
    print("You are adult and you can buy alcohol")
else:
    print("you are too young to buy alcohol")

age = 15

if age >= 18:
    print("You are adult and you can buy alcohol")
else:
    print("You are too young to buy alcohol")

isDrunk = False
if age >= 18 and not isDrunk:
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")

age = 27

isDrunk = False
if age >= 18 and not isDrunk:
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")
'''

age = 27

isDrunk = True
if age >= 18 and not isDrunk:
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")

isRestrictedArea = False

isDrunk = False
if age >= 18 and not isDrunk and not isRestrictedArea:
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")