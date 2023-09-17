import random

print("Welcome to Number Guessing Game")
print("Guess a number between 1 to 100 ")
level = input("Choose a easy or hard level: ").lower()

choice = random.randint(1,100)
print(f"Psst! {choice}")

def logic(n):
  
  if int(choice-10) < int(n) < int(choice+10):
    print("You are very close. ")
  elif int(choice-20) < int(n) < int(choice+20):
    print("You are little closer.")
  elif int(choice-30) < int(n) < int(choice+30):
    print("You are little farway. ")
  elif int(choice-40) < int(n) < int(choice+40):
    print("You are farway. ")
  else:
    print("You are far farway. ")

if level == 'hard':
    n = 5
elif level == 'easy':
    n = 6
print(f"You have {n} guesses in total")

while n:
  a = int(input("Guess a number: "))

  if a == choice:
    print("Guessed correct! Game Over!")
    break;
    
  else:
    logic(a)
    n= n-1
    print(f"You have {n} attempts left ")
    if n == 0:
      print("Out of guesses. You lose")
