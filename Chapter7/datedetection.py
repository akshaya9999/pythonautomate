from builtins import int
import re
inp=input("enter date") #regex code to input basic date
yearRegex=re.compile(r'^([1-2][0-9]|3[0-1])\/([0-1][0-9])\/([1-2]\d{3})$')
mo = yearRegex.search(inp)
day,month,year=mo.groups()
f=0
def isleapyear(y):
    if (y % 400 == 0) and (y % 100 == 0):
        return 1
    elif (y % 4 ==0) and (y % 100 != 0):
        return 1
    else:
        return 0
w=isleapyear(int(year))


if w==1 and month=='02' and int(day)<=29:
    f==1
elif month=='02' and int(day)<=28:
    f==1
elif month in ['01','03','05','07','08','10','12'] and int(day)>0 and int(day)<=31:
    f=1
elif month in ['04','06','09','11'] and int(day)>0 and int(day)<=30:
    f=1
if int(year) <1000 or int(year)>2999:
    f=0
if f==1:
    print("valid date")
else:
    print("not valid date")





