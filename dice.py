# Name: Cassandra Criger
# Period 6
# Dice Rolling Simulator
import random

side1 = 0
side2 = 0
side3 = 0
side4 = 0
side5 = 0
side6 = 0

print("Welcome to Dice Simulator")
rolls = int(input("How many times do you wanna roll?: "))
x = 1

while x <= rolls:
  roll = random.randint(1,6)
  if roll == 1:
    side1 += 1
    print("result is 1")
  elif roll == 2:
    side2 += 1
    print("result is 2")
  elif roll == 3:
    side3 += 1
    print("result is 3")
  elif roll == 4:
    side4 += 1
    print("result is 4")
  elif roll == 5:
    side5 += 1
    print("result is 5")
  elif roll == 6:
    side6 += 1
    print("result is 6")
  x = x + 1

print("The dice was rolled " + str(rolls) + " times.")
print(str(side1) + "\n" + str(side2) + "\n" + str(side3) + "\n" + str(side4) + "\n" + str(side5) + "\n" + str(side6))
math1 = side1/rolls * 100
math2 = side2/rolls * 100
math3 = side3/rolls * 100
math4 = side4/rolls * 100
math5 = side5/rolls * 100
math6 = side6/rolls * 100
print(str(math1) + "%" + "\n" + str(math2) + "%" + "\n" + str(math3) + "%" + "\n" + str(math4)  + "%" + "\n" + str(math5)  + "%" + "\n" + str(math6)  + "%")
