import sys
import random
print('ROCK, PAPER, SCISSORS')
wins=0
losses=0
ties=0
while True:
  print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
  while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    playerMove=input()
    if(playerMove=='q'):
      sys.exit()
    if(playerMove=='r'or playerMove=='p'or playerMove=='s'):
      break
    print('Type one of r, p, s, or q.')
    
  sysPlays=random.randint(1,3)
  if(sysPlays==1):
    sysMove='r'
    tieGame='Rock'
  elif(sysPlays==2):
    sysMove='p'
    tieGame='Paper'
  else:
    sysMove='s'
    tieGame='Scissors'
    
# Display and record the win/loss/tie: 
  if playerMove==sysMove:
    print(tieGame,'versus',tieGame)
    print('It is a tie!')
    ties = ties + 1
  elif playerMove == 'r' and sysMove == 's':
    print('Rock versus Scissors')
    print('You win!')
    wins = wins + 1
  elif playerMove == 'p' and sysMove == 'r':
    print('Paper versus rock')
    print('You win!')
    wins = wins + 1
  elif playerMove == 's' and sysMove == 'p':
    print('Scissors versus Paper')
    print('You win!')
    wins = wins + 1
  elif playerMove == 'r' and sysMove == 'p':
    print('Rock versus Paper')
    print('You lose!')
    losses = losses + 1
  elif playerMove == 'p' and sysMove == 's':
    print('Paper versus Scissors')
    print('You lose!')
    losses = losses + 1
  elif playerMove == 's' and sysMove == 'r':
    print('Scissors versus Rock')
    print('You lose!')
    losses = losses + 1