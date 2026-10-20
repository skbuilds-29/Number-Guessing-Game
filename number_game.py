import random
b = True
secret_number = random.randint(1,100)
num_guesses = 0
while b:
    guess = int(input( "Enter your guess! "))
    if(guess<secret_number and guess>0):
        print("Too low! (Guess higher)")
    elif(guess>secret_number and guess<=100):
        print("Too high! (Guess lower)!")
    elif(guess==secret_number):
        print("You Win!")
        b = False
    else:
        print("Invalid guess! Please enter a number between 1 and 100!")
    num_guesses+=1
print("It took you " + str( num_guesses) + " guesses")
