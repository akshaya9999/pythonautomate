import re
f=1
passw=input("enter password")
eightch=re.compile(r'\w{8}')
hasupperc=re.compile(r'[A-Z]+')
haslower=re.compile(r'[a-z]+')
hasdigit=re.compile(r'[0-9]+')
if eightch.findall(passw)==[]:
    f=0
elif hasupperc.findall(passw)==[]:
    f=0
elif haslower.findall(passw)==[]:
    f=0
elif hasdigit.findall(passw)==[]:
    f=0
if f==1:
    print("password is strong")
else:
    print("password is not strong")
