import math

record = float(input())
distanceM = float(input())
secondsForM = float(input())

timeInSec = distanceM * secondsForM
slownes = math.floor(distanceM / 15) * 12.5
totalTime = timeInSec + slownes

if totalTime < record:
    print(f"Yes, he succeeded! The new world record is {totalTime:.2f} seconds.")
else:
    needTime = totalTime - record
    print(f"No, he failed! He was {needTime:.2f} seconds slower.")
