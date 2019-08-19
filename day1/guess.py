# Author: Qiaoguo Zhang

age_of_oldboy = 56
'''
guess_age = int(input("guest age:"))

if guess_age == age_of_oldboy:
    print("yes, you got it.")
elif guess_age > age_of_oldboy:
    print("think smaller...")
else:
    print("think bigger!...")
'''

count = 0
'''
while count < 3:
    guess_age = int(input("guest age:"))
    if guess_age == age_of_oldboy:
        print("yes, you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger!...")
    count += 1
else:
    print("you have tried too many times.. fuck off")
'''

for i in range(3):
    guess_age = int(input("guest age:"))
    if guess_age == age_of_oldboy:
        print("yes, you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger!...")
else:
    print("you have tried too many times.. fuck off")