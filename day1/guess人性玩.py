# Author: Qiaoguo Zhang

age_of_oldboy = 56

count = 0
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
    if count == 3:
        counine_confirm = input("do you want to keep guessing...?")
        if counine_confirm != "n":
            count = 0

else:
    print("you have tried too many times.. fuck off")