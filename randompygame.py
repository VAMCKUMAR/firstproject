import sys
from random import randint
print('Guess a number from 1 to 10')
answer = randint(int(sys.argv[1]), int(sys.argv[2]))


while True:
	try:
	  print(answer)
	  guess = int(input('Guess the number from {sys.arg[1]} - {sys.argv[2]}  : '))
	  if 0 < guess < 11:
		  if guess == answer:
			  print("you are a genious")
			  break
		  else:
		  	print("Try again")
	except ValueError:

		print("Enter the number from 1-10")
		continue
