spam=[]
print("enter values in list or enter nothing to move to next step")
while True:
    s=input()
    if not s:
        break
    spam.append(s)
l=len(spam)
for i in range (0,l):
    if(i==(l-1)):
        print(spam[i])
    elif(i!=l-2):
        print(spam[i],end=",")
    else:
        print(spam[i],",and ",end="")