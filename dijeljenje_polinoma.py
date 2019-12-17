try:
    from itertools import izip 
except ImportError: 
    izip = zip  #ako ne pronade 

def degree(poly):
    while poly and poly[-1] == 0:
        poly.pop()   # brisemo element kojeg smo obradili
    return len(poly)-1

def poly_div(N, D):
    dD = degree(D) #broj clanova u nizu
    dN = degree(N)
    if dD < 0: raise ZeroDivisionError #provjera da nazivnik nije jednak 0
    if dN >= dD: #provjeravamo jeli djeljenik veci od djeljitelja
        q = [0] * dN
        while dN >= dD:
            d = [0]*(dN - dD) + D
            mult = q[dN - dD] = N[-1] / float(d[-1])
            d = [coeff*mult for coeff in d]
            N = [( coeffN - coeffd ) for coeffN, coeffd in izip(N, d)]
            dN = degree(N)
        r = N
    else: #ako je djeljitelj veci od djeljenika
        q = [0]
        r = N
    return q, r #vracamo rezultat i ostatak
    

if __name__ == '__main__':
    print ("POLYNOMIAL LONG DIVISION")
    N = [2, -1, -2, 3] #navedeni su brojevi koeficjenata uz 'x', a pozicija u nizu oznacava stupanj; pozicija 0 -> stupanj polinoma 0
    D = [1, -1]
    print ("  %s / %s =" % (N,D)),
    print (" %s remainder %s" % poly_div(N, D)) #ispis rjesenja