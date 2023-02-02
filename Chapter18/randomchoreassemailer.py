import random
import ezgmail

l=[]
l=input("enter emails with spaces").split()
for i in l:

    chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
    randomChore = random.choice(chores)
    chores.remove(randomChore)
    ezgmail.send(i,'chore to do','your chore is '+randomChore)