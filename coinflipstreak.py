import random
numberOfStreaks = 0
h=[]
tt=0
hh=0
c=0
for experimentNumber in range(10000):   #for outer 10000 cases
    tt=0
    hh=0
    for i in range (0,92):      #creating 100 h or t
        s=random.randint(1,2)
        if(s==1):
            h.append('H')
        else:
            h.append('T')
        for k in h:
            if(k=="H"):
                c+=1
            else:
                c=0
        if(c==6):
            numberOfStreaks+=1
                
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))