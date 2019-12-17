def Subtract(gen,remain): #Metoda oduzimanja izvodi bitovni XOR između generatora i ostatka
    rem= []
    for x in range(0,len(gen)):
        rem.append(int(gen[x]^remain[x]))
    return rem

def Carrythrough(gen,mes,encode = True):
    '''Ova metoda obavlja glavne operacije CRC-a, a upotrebljava se i kod funkcije Encode i Verify'''
    print(mes)
    quotient = []
    message = []
    generator = []
    for char in mes:
        message.append(int(char,2))     #Pretvara poruku u niz bitova
    for char in gen:
        generator.append(int(char,2))   #Pretvara generator u listu bitova
    if encode == True:                  #Dodaje 0 na poruku ako se koristi za encode funkciju
        for x in range(len(gen)-1):
            message.append(0)
    remainder = message[0:len(generator)]
    index = 0
    while index+len(generator) < len(message):   # Izvršava se dok god ima bitova u prijenosnoj sekvenci
        if remainder[0] == 1:                     #Ako je element na prvom indeksu u ostatku 1, dodaj 1 u kvocijent

            quotient.append(1)                      #I onda od remindera oduzmi generator
            remainder = Subtract(generator,remainder)
        else:
            quotient.append(0)
        remainder.pop(0)                                    #uklanja prvu 0 iz ostatka
        remainder.append(message[index+len(generator)])     
        index+=1
    if remainder[0] ==1:
        remainder = Subtract(generator,remainder)
    remainder.pop(0)
    for item in remainder:
        mes+=str(item)
    return(mes)

def Encode():
    '''Ova metoda uzima poruku kao niz 1 i 0 i i generator polinom i stvara prijenos u obliku izvornog postupka
    s provjerom'''

    mes = str(input("Enter message for transmission (in string of 1's and 0's): "))
    gen = str(input("Enter Generator Polynomial Coefficients as (in string of 1's and 0's): "))

    print('Transmission: '+Carrythrough(gen,mes))
    print('Generator: ' +gen)

def Verify():
    '''Metoda za potvrđivanje uzima prijenosnu sekvencu kao string jedinica i nula i 
    generira polinom, i provjerava taj polinom na greške s generatorom (sekvencom 0 i 1)'''
    mes = str(input("Enter transmission for error detection (in string of 1's and 0's: "))
    gen = str(input("Enter Generator Polynomial (string of 1's and 0's): "))

    detection = Carrythrough(gen,mes,False) #poziva Carrythrough funkciju sa False za enkodiranje kako ne bi dodavao 0 na kraj prijenosa
    if int(detection[len(mes):]) != 0:      
        print("There is an error")
    else:
        print("No errors detected")

def main():
    '''Glavna funkcija daje korisnicima mogućnost odabira kodiranja ili potvrde funkcije'''
    choice = str(input("Encode or Verify? (Enter E for encode, V for verify): "))
    if choice.lower() == 'e':
        Encode()
    elif choice.lower() == 'v':
        Verify()
    else:
        main()
main()