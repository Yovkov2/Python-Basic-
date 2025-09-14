budget = float(input())
graphicsCards = int(input())
procesors = int(input())
ram = int(input())

graphicsCardsPrice = graphicsCards * 250
procesorsPrice = graphicsCardsPrice * 0.35
ramPrice  = graphicsCardsPrice * 0.1

procesorsSum = procesors * procesorsPrice
ramSum = ram * ramPrice
total = graphicsCardsPrice + procesorsSum + ramSum


if graphicsCards > procesors:
    total *= 0.85


if total <= budget:
    leftMoney = budget - total
    print(f"You have {leftMoney:.2f} leva left!")
else:
    needMoney = total - budget
    print(f"Not enough money! You need {needMoney:.2f} leva more!")
