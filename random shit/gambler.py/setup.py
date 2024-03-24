from os import system
import random
import time

class gambler():
    def __init__(self, name):
        self.name = name
        self.balance = 100 # todo: pas dit aan naar het bedrag uot gamblers.sqlite3
        
    def __str__(self):
        return(f'{self.name} has a balance of {self.balance}')
    
    def checkBetAmount(self, betAmount):
        if betAmount > self.balance:
            return False, 'dont got the cash'
        elif betAmount <= 0:
            return False, 'cant bet nothin'
        else:
            return True, 'all right'
    
    def slots(self, betAmount):
        sym = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        wonBack = 0
        doubleSpin = False
        
        print(f'2 the same: bet*2.5\n3 the same (except the below): bet*7.5\n111: bet*15\n222: bet*10\n333:double the spin, double the win')
        
        input('press enter to SPINNN')
        
        X = random.choice(sym)
        Y = random.choice(sym)
        Z = random.choice(sym)
        
        roll = f'{X}{Y}{Z}'
        print(f'roll: {roll}')
        
        
        furtherX = furtherY = furtherZ = True
        for slot in sym:
            system('cls')
            slots = '|'
            
            if slot != X and furtherX == True:
                slots += slot
            else:
                furtherX = False
                slots += X
                
            slots += '|'
                
            if slot != Y and furtherY == True:
                slots += slot
            else:
                furtherY = False
                slots += Y
                
            slots += '|'
                
            if slot != Z and furtherZ == True:
                slots += slot
            else:
                furtherZ = False
                slots += Z
                
            slots += '|'
                
            print(slots)
            
            if slots == roll:
                break
            
            time.sleep(0.3)
            
        for i in range(0,11):
            count = slots.count(str(i))
            print(count, i, slots)
            
            if count == 2:
                wonBack = betAmount * 2.5
                break
            elif count == 3:
                if slots == '111':
                    wonBack = betAmount*15
                elif slots == '222':
                    wonBack = betAmount*10
                elif slots == '333':
                    doubleSpin = True
                else:
                    wonBack = betAmount*7.5
                    
        