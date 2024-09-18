# start

import random

lottery = random.randint(1, 100)
print(lottery)
num: int = int(input("number : "))
while True:
    if num < lottery:
        print("yore number is too small")
        num: int = int(input("number : "))
    elif num > lottery:
        print("yore number is too big")
        num: int = int(input("number : "))
    else:
        print("bingo")
        break

# stop
