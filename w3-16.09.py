# start

num: int = int(input("number : "))
for i in range(1, num + 1, 1):
    for i in range(i):
        print(i, end=" ")
    print(" ")
for i in range(num - 1, 1, -1):
    for i in range(i):
        print(i, end=" ")
    print(" ")

# איתי איך  זה הגיוני שצינתי ספרה 1 וזה מתחיל מספרה 0
