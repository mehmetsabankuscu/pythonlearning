"""
ikinci derececeden
denklemelerde 
kök bulma

denklem ax^2+bx+c

delta hesablama: b^2-4ab

kök1:-b-delta**0.5/(2*a)
kök2:-b+delta**0.5/(2*a)

"""

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))


delta = b**2-4*a*c

kok1 = -b-delta**0.5/(2*a)
kok2 = -b+delta**0.5/(2*a)

print("birinci kök değeri: {}\nikinci kök değeri: {}\n    **** hepsi bu kadar ***".format(kok1,kok2))