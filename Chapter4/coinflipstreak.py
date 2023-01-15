import random
numberOfStreaks = 0
ht=[]
n=0
for experimentNumber in range(10):
    for i in range(100):
        s=random.randint(0,1)
        if(s==0):
            ht.append('H')
        else:
            ht.append('T')
    #print(len(ht))  #each len(ht) is 100 ie in one iteration len is 100
    for j in range(n,len(ht)-1):   #1st loop iterates 1st 100 elements,then the next 100
        try:                       #given n to start from 100 then 200 and so on
            if ht[j]==ht[j+1]==ht[j+2]==ht[j+3]==ht[j+4]==ht[j+5]:
                numberOfStreaks+=1
            n+=100
            #print(n)    #n has to go from 100 to 200 ...
        except:
            break       #to catch any index


print('Chance of streak: %s%%' % (numberOfStreaks / 100))