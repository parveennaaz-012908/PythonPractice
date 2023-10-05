import random
import logging

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug('Start the program')
    guess=''
    while True:
        logging.debug('Start the Guess!!')
        print('Guess the coin toss! Enter heads or tails: ')
        guess = input()

        logging.debug('Start the tossing Coin!!')
        toss=random.randint(0,1)
        logging.debug('Does ' + str(toss) + ' equal ' + str(guess) + '?')
        if toss == 0 and guess =='heads':
            print('You got it!')
        print('Nope! Guess again!')
        guesss = input()
        elif toss == 1 and guess=='tail':
        print('You got it!')