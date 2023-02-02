from builtins import int
import sys


cd={}
kl=[]
actualcount={'wking':1,'wqueen':1,'wrook':2,'wbishop':2,'wknight':2,'wpawn':8,'bking':1,'bqueen':1,'brook':2,'bbishop':2,'bknight':2,'bpawn':8}
finalcount={}
def isValidChessBoard(cd):
    kk=cd.keys()
    for i in range(97,105): #to create the spaces in the board
        for j in range(1,9):
            kl.append(chr(i)+str(j))

    # print(kl)
    x=cd.keys() #to check if its a valid key
    if(all(x in kl for x in cd)): 
        y1=1
        # print(cd)
        for x in cd.values(): #counting no of pieces and putting it in a new dict
            finalcount.setdefault(x, 0)
            finalcount[x]=finalcount[x]+1
            # print(finalcount)
            for l in finalcount.keys():
                if finalcount[l]<=actualcount[l]:
                    print("is valid")
                else:
                    print("is not valid")
    else:
        print("board has an invalid space")
        sys.exit()

while True:
    e=int(input("enter 1 to input values 2 to check if valid and 3 to exit"))
    if e==1:
        k,v=input("enter space and piece name with spaces").split()
        cd[k]=v
    elif e==2:
        isValidChessBoard(cd)
    elif e==3:
        break
# isValidChessBoard(cd)
