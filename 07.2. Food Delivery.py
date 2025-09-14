#• Пилешко меню – 10.35 лв.
#• Меню с риба – 12.40 лв.
#• Вегетарианско меню – 8.15 лв.

chikenQuantity = float (input())
fishQuantity = float (input())
veganQuantity = float (input())


chikenSum = chikenQuantity * 10.35
fishSum = fishQuantity * 12.40
veganSum = veganQuantity * 8.15
menuSum = chikenSum + fishSum + veganSum

desertPrice = menuSum * 0.2

finalSum = menuSum + desertPrice
total = finalSum + 2.50

print(f"Цена на поръчката:  {total: .2f} ")
