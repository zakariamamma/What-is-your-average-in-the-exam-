import random
print("\033[32m lets play the game \033[0m")

def guess_the_number():
  """Plays a simple guessing game where the user tries to guess a random number."""

  number = random.randint(1, 100)  # Generate a random number between 1 and 100
  guesses_left = 7 
  print("I'm thinking of a number between 1 and 100.")

  while guesses_left > 0:
    try:
      guess = int(input("Take a guess: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue  # Go back to the beginning of the loop

    if guess < number:
      print("Too low! You have", guesses_left - 1, "guesses left.")
    elif guess > number:
      print("Too high! You have", guesses_left - 1, "guesses left.")
    else:
      print("Congratulations! You guessed it in", 7 - guesses_left, "tries.")
      return  # End the game

    guesses_left -= 1

  print("You ran out of guesses! The number was", number)

# Start the game
guess_the_number()
