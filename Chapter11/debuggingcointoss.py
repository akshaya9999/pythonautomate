import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s -  %(message)s')
logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('start of loop')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss==0:
    toss='tails'
else:
    toss='heads'
logging.debug('toss='+ str(toss))
logging.debug('guess='+str(guess))
if toss == guess:
    print('You got it!')
    logging.debug('toss==guess')
else:
    print('Nope! Guess again!')
    logging.debug('not equal')
    guesss = input()
    logging.debug('toss='+ str(toss))
    logging.debug('guess='+str(guess))
    if toss == guess:
        print('You got it!')
        logging.debug('correct the 2nd time')
    else:
        print('Nope. You are really bad at this game.')
        logging.debug('not equal 2nd time')