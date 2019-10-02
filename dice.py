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
rolls = random.random(1,6)

print("Welcome to Dice Simulator")
pName = input("How many times do you wanna roll?: ")

while True:
	
	printScore()
	if pMove == "q":
		break
	cMove = random.choice(cMoves)
	if pMove == "r":
		print(pName + "picked Rock")
	    if cMove == "rock":
	    	print("Computer picks Rock")
	    	print("Tie")
	    	ties += 1
	    elif cMove == "paper":
	    	print("Computer picks Paper")
	    	print("Computer wins")
	    	cScore += 1
	    else cMove == "scissors":
	    	print("Computer picks Scissors")
	    	print("You won")
	    	pMove += 1
	elif pMove == "p":
		print(pName + "picked Paper")
	    if cMove == "paper":
	    	print("Computer picks Paper")
	    	print("Tie")
	    	ties += 1
	    elif cMove == "rock":
	    	print("Computer picks Rock")
	    	print("You wins")
	    	cScore += 1
	    else cMove == "scissors":
	    	print("Computer picks Scissors")
	    	print("Computer won")
	    	pMove += 1
	elif pMove == "s":
		print(pName + "picked Scissors")
	    if cMove == "scissors":
	    	print("Computer picks Scissors")
	    	print("Tie")
	    	ties += 1
	    elif cMove == "paper":
	    	print("Computer picks Paper")
	    	print("You wins")
	    	cScore += 1
	    else cMove == "rock":
	    	print("Computer picks Rock")
	    	print("Computer won")
	    	pMove += 1
	else:
		print("That is not an option")
