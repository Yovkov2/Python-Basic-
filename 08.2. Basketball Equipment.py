taxPerYear = float (input())

shoes = taxPerYear - (taxPerYear * 0.4)
equip = shoes - (shoes * 0.2)
ball = equip *  0.25
accessories = ball * 0.2

total = taxPerYear + shoes + equip + ball + accessories
print(total)