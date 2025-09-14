nameFilm = input()
lenghtEpisode = int(input())
breakTime = int(input())

timeForLunch = breakTime * 0.125   # 1/8 от почивката
chillTime = breakTime * 0.25       # 1/4 от почивката
leftTime = breakTime - timeForLunch - chillTime


import math
leftTimeCeil = math.ceil(leftTime)
needTimeCeil = math.ceil(abs(leftTime - lenghtEpisode))

if leftTime >= lenghtEpisode:
    print(f"You have enough time to watch {nameFilm} and left with {needTimeCeil} minutes free time.")
else:
    print(f"You don't have enough time to watch {nameFilm}, you need {needTimeCeil} more minutes.")
