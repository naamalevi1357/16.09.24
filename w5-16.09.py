# start

x: int = int(input("number 1:"))
mona: int = 0

while x % 7 == 0:
    if x % 11 == 0:
        break
    mona += 1
    x: int = int(input("number  :"))
else:
    print(f"name {mona} ")

# stop

# start

num: int = int(input("number :"))
x: bool = num % 5 == 0
y: bool = num % 3 == 0
z: bool = num % 5 == 0 and num % 3 == 0
if z:
    print("fizz buzz")
elif y:
    print("buzz")
elif x:
    print("fizz ")

# stop
