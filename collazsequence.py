import sys
def collats(number):
    if(number%2==0):
        print(number//2)
        return (number//2)
    else:
        print(3*number+1)
        return(3*number+1)
while(True):
    try:
        while(True):
            n=int(input("enter no"))
            x=collats(n)
            if(x==1):
                sys.exit()      
    except ValueError:
        print("enter an integer")
        continue
    
