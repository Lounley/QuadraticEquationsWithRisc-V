import math

#DTEK0063 Processor Architetures Project
def quadraticcalc(a,b,c):
    inroot = b*b-4*a*c

    #if answer is complex
    if inroot < 0:
        return
    sqrt = math.sqrt(inroot)

    print((- b + sqrt)/(2*a))
    print((- b - sqrt)/(2*a))


a = 6
b = 8
c = -2

quadraticcalc(a,b,c)
