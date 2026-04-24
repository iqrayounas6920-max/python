import random
attempt=5
game =int(input ("Enter game level:"))
if game <=50:
    print("Easy level start")
elif game <=100:
    print("medium level start")

elif game <=200:
        print("Difficult level")
else:
    print("Game Over") 
     
choice =(input("enter choice:"))
if choice == "1":
 number = random.randint(1,50)
 attempt =5
elif choice == "2":
  number = random.randint(1,100)
  attempt =3
elif choice == "3":
 number = random.randint(1,200)
 attempt =5
if choice == "4":
 print("Good bye")
while attempt >0:
    guess =int(input("enter guess:"))
    if guess==number:
        print("Win")
        break
    else:
        print("loss")
        attempt-=1
        print("Attempts left:", attempt)

if attempt == 0:
    print("Game Over")



    
