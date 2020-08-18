# Sarthak Gupta
# 6/7/2018
# Calculates the win probability of a battle in RISK: Global Domination

from random import seed
from random import randint

offDie = int(input('Number of Offensive Dice: '))
defDie = int(input('Number of Defensive Dice: '))

winDefensive = 0
winOffensive = 0

# recurvisely runs through the loop 5000 times to check to see how many times this battle was won
count = 5000

oLeft = 0

for i in range(0,count):
    defDieCount = defDie
    offDieCount = offDie - 1
    
    while defDieCount!=0 and offDieCount!=0:
        if defDieCount>=2:
            dList = [randint(1,6), randint(1,6)]
        else:
            dList = [randint(1,6)]

        if offDieCount>=3:
            oList = [randint(1,6), randint(1,6), randint(1,6)]
        elif offDieCount==2:
            oList = [randint(1,6), randint(1,6)]
        else:
            oList = [randint(1,6)]
        
        while len(dList)!=0 and len(oList)!=0:
            dList.sort(reverse=True)
            oList.sort(reverse=True)
            
            if dList[0]>=oList[0]:
                offDieCount = offDieCount - 1
                dList.pop(0)
                oList.pop(0)
            else:
                defDieCount = defDieCount - 1
                dList.pop(0)
                oList.pop(0)

    oLeft = oLeft + offDieCount

    if defDieCount > 0:
        winDefensive = winDefensive + 1
    else:
        winOffensive = winOffensive + 1

oLeftAverage = oLeft / count

# print('Offensive wins:', winOffensive)
# print('Defensive wins:', winDefensive)
print()

print('Predicted offensive troops remaining:', int(oLeftAverage - 1))

print("PROBABILITY OF WINNING:", (winOffensive/(winOffensive+winDefensive))*100, "%")
print()
