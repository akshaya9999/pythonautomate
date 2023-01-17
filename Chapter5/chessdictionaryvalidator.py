from builtins import int
import sys
cd={}
kl=[]
count={}
def isValidChessBoard(cd):
    kk=cd.keys()
    for i in range(97,105):   #to create the spaces in the board
        for j in range(1,9):
            kl.append(chr(i)+str(j))
    x=cd.keys()           #to check if its a valid key
    
    if(all(x in kl for x in cd)):     
        for x in cd.values():     #counting no of pieces and putting it in a new dict
            count.setdefault(x, 0)
            count[x]=count[x]+1
            print(count)   #error in condition have to find a way to give or and and the right way
        if(count['wking']<=1 and count['wqueen']<=1 and count['wrook']<=2 and count['wbishop']<=2 and count['wknight']<=2 and count['wpawn']<=8 or count['bwking']<=1 and count['bqueen']<=1 and count['brook']<=2 and count['bbishop']<=2 and count['bknight']<=2 and count['bpawn']<=8):
            print(True)
        else:
            print(False)
    else:
        print("board has an invalid space")
        sys.exit()

while True:
    e=int(input("enter 1 to input values 2 to check if valid and 3 to exit"))
    if e==1:
        k,v=input("enter space and piece name with spaces").split()
        cd[k]=v
    elif(e==2):
        isValidChessBoard(cd)
    elif e==3:
        break
isValidChessBoard(cd)
