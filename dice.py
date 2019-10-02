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
roll = random.random(1,6)

print("Welcome to Dice Simulator")
rolls = input("How many times do you wanna roll?: ")

while True:

  if roll == "1":
    side1 += 1
  elif roll == "2":
    side2 += 1
  elif roll == "3":
    side3 += 1
  elif roll == "4":
    side4 += 1
  elif roll == "5":
    side5 += 1
  else roll == "6":
    side6 += 1
