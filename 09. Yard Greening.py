cubeMetters = float (input())
cubeMetterPrice = 7.61

firstSum = cubeMetters * cubeMetterPrice
discount = firstSum * 0.18
finalSum = firstSum - discount

print(f"The final price is: {finalSum} lv")
print(f"The discount is: {discount} lv.")