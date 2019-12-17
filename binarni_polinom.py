def bitstring(x): 
    
    return bin(x)[2:] #pretvaramo integer u binarni niz

def printlongdiv(lhs, rhs):
    
    rem = lhs #zadane vrijednosti
    div = rhs
    origlen = len(bitstring(div)) #broj bitova u djeljitelju
    

    # pomak ulijevo
    count = 1
    while (div | rem) > 2*div: #usporedujemo inkluzivno ILI izmedu unesenih vrijednosti sa dvostrukim djeljenikom 
        div <<= 1 #vršimo pomak ulijevo i pridajemo vrijednost lijevom operandu
        count += 1
    
    # dijelimo sve dok se ne vratimo tamo gdje smo zapoceli
    quot = 0
    while count>0:
        quot <<= 1
        count -= 1
        print("%14s" % bitstring(rem))
        divstr = bitstring(div) #broj bitova u djeljeniku

        if (rem ^ div) < rem: #usporedujemo ekskluzivno ILI izmedu unesenih vrijednosti sa djeljiteljem
            quot |= 1
            rem ^= div

            print(1, " " * (11-len(divstr)), divstr[:origlen])
        else:
            print(0, " " * (11-len(divstr)), "0" * origlen)

        print(" " * (13-len(divstr)), "-" * origlen)
        div >>= 1

    print("%14s <<< remainder" % bitstring(rem)) #ispis ostatka
    print(" -> %10s <<< quotient" % bitstring(quot)) #ispis rjesenja
    

if __name__ == '__main__':
    printlongdiv(53, 6) #zadajemo vrijednosti