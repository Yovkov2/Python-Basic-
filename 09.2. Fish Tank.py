lenght = float (input())
wight = float (input())
hight = float (input())
procent = float (input())

volume = lenght * wight * hight
volumeInLiters = volume / 1000
procentSum = (1- procent / 100)

result = volumeInLiters * procentSum
print(result)
