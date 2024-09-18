# start


sum_temp: int = 0
for _ in range(5):
  temp: int = int(input("what is temperature?"))
  while temp< -50 or temp>45:
        temp: int = int(input("what is temperature?"))
  else:
      sum_temp =+ temp
print(sum_temp / 5)

# stop
