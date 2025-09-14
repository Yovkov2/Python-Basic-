budget = float(input())
statist = int(input())
dressPrice = float(input())

decorSum = budget * 0.1
dressSum = statist * dressPrice

if statist > 150:
    dressSum *= 0.9   # прилагаме 10% отстъпка

firstSum = decorSum + dressSum

if firstSum <= budget:
    leftMoney = budget - firstSum
    print("Action!")
    print(f"Wingard starts filming with {leftMoney:.2f} leva left.")
else:
    needMoney = firstSum - budget
    print("Not enough money!")
    print(f"Wingard needs {needMoney:.2f} leva more.")
