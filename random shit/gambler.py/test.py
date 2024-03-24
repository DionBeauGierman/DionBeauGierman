
def testSlots(slots, betAmount = 150):
    doubleSpin = False
    
    wonBack = 0
    for i in range(0,11):
        count = slots.count(str(i))
            
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
        
    print(wonBack, doubleSpin)
        
testSlots('111')
testSlots('222')
testSlots('333')
testSlots('444')
testSlots('395')
testSlots('242')
testSlots('224')
testSlots('422')
