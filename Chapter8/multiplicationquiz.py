import random, time
import threading
number_Questions = 10
answer = 0
i = 0
c=0
sctn=0
for questionNumber in range(1, (number_Questions + 1)):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    questionNumber = f"#{questionNumber} : {num1} * {num2}\n"
    print(questionNumber)
    def sctn():
        print("time is up")
        print("enter ans")
    timer =threading.Timer(8.0,sctn)
    timer.start()
    for i in range(1,4):
        answer=input()
        timer.cancel()
        if sctn ==1:
            continue

        if answer==str((num1*num2)):
            c+=1
            print('correct')
            
            time.sleep(1)
            break
        else:
            print('incorrect ,try again')
print("no of correct ans:",c)