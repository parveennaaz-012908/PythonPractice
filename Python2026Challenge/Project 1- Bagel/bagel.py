# This project is for guessing the right number.Its deducing the number to find the right number.

from GeneralMethod import getRandomNum


num_digit = 3
max_guesses = 10


def main():
    print(''' Bagels, a deductive logic game
          I am thinking of a {}-digit number with no repeated digits.
            Try to guess what it is. Here are some clues:
            When I say:     That means:
            Pico            One digit is correct but in the wrong position.
            Fermi           One digit is correct and in the right position.
            Bagels          No digit is correct.
        For example, if the secret number was 248 and your guess was 843, the
        clues would be Fermi Pico.'''.format(num_digit)
        )
   
    secret_num=getRandomNum(num_digit)
    print("I am thinking of a 3-digit number.")
    print("You have 10 guesses.")
    
    for i in range(max_guesses):
        guess = input("Guess: ")
        
        if len(guess)==3 and guess.isdigit():
            result=getClues(guess,secret_num)
            print(result)
        else:
            print("Enter a valid 3-digit number.")
      
    else:
        print("Out of guesses!")
        print(f"The secret number was {secret_num}.")


    
  


def getClues(guess_num,secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess_num==secret_num:
        return f"You won in {guess_num} guesses!"
    clues=[]
    for i in range(len(guess_num)):
        if guess_num[i]==secret_num[i]:
            clues.append("Fermi")
        elif guess_num[i] in secret_num:
            clues.append("Pico")
        if not clues:
            return "Bagels"
    clues.sort()
    return " ".join(clues)
                
    


    

    



 

