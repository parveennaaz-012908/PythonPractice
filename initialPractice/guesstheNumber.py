import random
print( "I am thinking of a number between 1 and 20.")
randNum = random.randint(1,20)

print("Take a guess.")
for guessesTaken in range(1, 7):
  guessNum=int(input())
  if(guessNum==randNum):
    print("Good job! You guessed my number in", guessesTaken ,"guesses!")
    break
  elif(guessNum<randNum):
    print('Your guess is too low.')
  elif(guessNum>randNum):
    print('Your guess is too high.')
  else:
    print('Your guess is wrong')