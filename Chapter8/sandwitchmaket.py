import pyinputplus as pyip
import re
prices = {'wheat': 10, 'white': 12, 'sour dough': 15, 'chicken': 20, 'turkey': 30, 'ham': 35, 'tofu': 15,'cheddar': 8, 'swiss': 9, 'mozzarella': 10, 'mayo': 5, 'mustard':6 , 'lettuce': 8,'tomato':5}
bread=pyip.inputMenu(['wheat','white','sourdough'],prompt='which bread\n')
protein=pyip.inputMenu(['chicken','turkey','ham','tofu'],prompt='which protein\n')
cheese=pyip.inputYesNo('want cheese?')
if cheese=='yes':
    cheesetype=pyip.inputMenu(['cheddar','swiss','mozzarella'],prompt='which cheese\n')
mayo = pyip.inputYesNo(' want mayo? \n')
mustard = pyip.inputYesNo(' want mustard? \n')
lettuce = pyip.inputYesNo('want lettuce? \n')
tomato = pyip.inputYesNo('want tomato ? \n')
nosand=pyip.inputInt(prompt='enter no of sandwitches\n',min=1)   
tot=0
print("prices are:")
for item in prices:
    p=prices[item]
    print(item,p)
    tot+=p
print("amount payable is:",tot*nosand)