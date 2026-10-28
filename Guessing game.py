import random
number=random.randint(1,100)
guessed_number= int(input("Enter a number(1-100): "))
if guessed_number <0 | guessed_number>100:
    print("INVAILD! PLEASE ENTER A CORRECT NUMBER ")
else:
    print("guessed_number:",guessed_number)
   

if guessed_number==number:
    print("YOU GUESS WAS RIGHT!!!")
    print("Random number: ",number)
else:
    print("BETTER LUCK NEXT TIME!")



