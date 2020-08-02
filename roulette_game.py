import random
initialAmount = 100
count = 0

while initialAmount > 0 :
    investAmount = int(input('bet Amount ? '))
    betNumber = input('bet on number ?')
    magicNumber = random.randint(0,10)
    
    if magicNumber == betNumber :
        initialAmount +=investAmount
    elif initialAmount >150:
            print('You Won')
            break
    elif initialAmount <50 :
            print('You Lose')
            break
    else :
            initialAmount = initialAmount - investAmount
            print('play Again')
     
    count +=1
    print('round ',count,' completed')