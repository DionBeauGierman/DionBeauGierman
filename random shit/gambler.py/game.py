import setup

setup.system('cls')

better = setup.gambler('Dion')
print(better)

bet = 50 #float(input('how much you willin to bet? '))
isGood, string = better.checkBetAmount(bet)

print(string)

if isGood == True:
    better.slots(bet)