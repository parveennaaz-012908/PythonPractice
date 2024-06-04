import sys, time
from textwrap import indent
if __name__ == '__main__':
    indent=0
    indentedIncreasing=True

try:
  while True:
    print(' ' * indent, end='')
    print('**********')
    time.sleep(0.1) # Pause for 1/10 of a second.
    if indentedIncreasing:
        indent= indent+1
        if indent==20:
            indentedIncreasing=False
    else:
        indent= indent-1
        if indent == 0:
         # Change direction:
            indentedIncreasing = True
except KeyboardInterrupt:
  sys.exit()
