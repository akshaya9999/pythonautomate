tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

maxlen=0
ml=[]
l1=len(tableData)
l2=len(tableData[0])      #l2  is length of each sublist ,given all have same length
l = [0] * l1      #l list creates list with same length
def printTable(data):
    for i in data:   #l is for storing length of each element 
        
        l=[]
        maxlen=len(i[0])
        for j in i:
          l.append(len(j))
        for k in l:
            if k>maxlen:
                maxlen=k
        ml.append(maxlen)
    maxx=ml[0]
    for q in ml:
      if q>maxx:
        maxx=q
    for k in range(l2):
      for l in range(l1):
        print(tableData[l][k].rjust(maxx), end = ' ')
      print()
printTable(tableData)