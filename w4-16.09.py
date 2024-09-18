# start

num: int = int(input("number : "))
y = ""
for i in range(1, num + 2, 2):
    for i in range(i):
        y += "*"
    print(f" {y:^10} ", end="  ")
    print("")
    y = ""

# stop
