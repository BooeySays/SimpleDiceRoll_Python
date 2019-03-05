#!/usr/bin/python

import random
#from six.moves import input as raw_input
#import sys, codecs
#sys.stdout = codecs.getwriter('utf_16')(sys.stdout.buffer, 'strict')

d1 = ('''
  [01;07;37;40m╭─────────╮[m
O [01;07;37;40m│         │[m
N [01;07;37;40m│    ●    │[m
E [01;07;37;40m│         │[m
  [01;07;37;40m╰─────────╯[m''')


d2 = ('''
  [01;07;37;40m╭─────────╮[m
T [01;07;37;40m│  ●      │[m
W [01;07;37;40m│         │[m
O [01;07;37;40m│      ●  │[m
  [01;07;37;40m╰─────────╯[m''')

d3 = ('''
T [01;07;37;40m╭─────────╮[m
H [01;07;37;40m│ ●       │[m
R [01;07;37;40m│    ●    │[m
E [01;07;37;40m│       ● │[m
E [01;07;37;40m╰─────────╯[m''')

d4 = ('''
F [01;07;37;40m╭─────────╮[m
O [01;07;37;40m│  ●   ●  │[m
U [01;07;37;40m│         │[m
R [01;07;37;40m│  ●   ●  │[m
  [01;07;37;40m╰─────────╯[m''')

d5 = ('''
F [01;07;37;40m╭─────────╮[m
I [01;07;37;40m│  ●   ●  │[m
V [01;07;37;40m│    ●    │[m
E [01;07;37;40m│  ●   ●  │[m
  [01;07;37;40m╰─────────╯[m''')

d6 = ('''
  [01;07;37;40m╭─────────╮[m
S [01;07;37;40m│  ●   ●  │[m
I [01;07;37;40m│  ●   ●  │[m
X [01;07;37;40m│  ●   ●  │[m
  [01;07;37;40m╰─────────╯[m''')

def printdice(x):
    print(' ')
    if x == 1:
        print(d1)
    elif x == 2:
        print(d2)
    elif x == 3:
        print(d3)
    elif x == 4:
        print(d4)
    elif x == 5:
        print(d5)
    else:
        print(d6)

#roll1 = random.randint(1,6)
#printdice(roll1)
#roll2 = random.randint(1,6)
#printdice(roll2)
#
##sumofdices = roll1 + roll2
#def totaldice(x, y):
#    sumofdices = x + y
#    if x == 1:
#        if y == 1:
#            print('\nYou rolled SNAKE EYES\n')
#    elif x != 1:
#        if x == y:
#            print('\nYou rolled a HARD ' + str(sumofdices) + '\n')
#        elif x != y:
#            print('\nYou rolled a SOFT ' + str(sumofdices) + '\n')
#    else:
#        print('error')
#        
#
#    
##    print('\nYou rolled a \033[01;32m' + str(sumofdices) + '\033[m\n\n')
#
#totaldice(roll1, roll2)
#

def rolling(x, y):
    rollnumber = x
    egg = y
    print('\n\tROLL NUMBER: ' + str(rollnumber))
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    totalsum = int(roll1) + int(roll2)
    if totalsum == egg:
        print('EASTER EGG')
        printdice(roll1)
        printdice(roll2)
    else:
        printdice(roll1)
        printdice(roll2)
    def totaldice(x, y):
        sumofdices = x + y
        if x == 1 and y == 1:
            print('\nYou rolled SNAKE EYES\n')
        elif x != y:
            print('\nYou rolled a SOFT ' + str(sumofdices) + '\n')
        elif x != 1:
            if x == y:
                print('\nYou rolled a HARD ' + str(sumofdices) + '\n')
        elif x != y:
            print('\nYou rolled a SOFT ' + str(sumofdices) + '\n')
        else:
            print('error')
    totaldice(roll1, roll2)
    rollagain_yn = input('[ Press the [ENTER] key to roll again, or [S] to stop ]\n\n: ')
    if rollagain_yn != 's' and rollagain_yn != 'S':
        print('\033c')
        rollnumber += 1
        rolling(rollnumber, rollagain_yn)
    else:
        print('Exiting')

rolling(1, 1)
