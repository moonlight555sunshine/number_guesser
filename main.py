import random
# Generate a random secret number between 1 and 100 (inclusive)
secret_number = random.randint(1, 101)
# Infinite loop to keep asking the user until they guess correctly
while True:
    number = input("Guess the number: ")
    try:
        number = float(number)   # Try to convert the input to a float
        if number.is_integer(): # Check if the number is an integer (not a float like 3.5)
            # Check if the number is within the allowed range
            if number < 0 or number > 100:
                print("It's not in range 0-100!")
                continue
            # Compare the number to the secret number
            if number < secret_number:
                print("Too small!")
                continue
            if number > secret_number:
                print("Too big!")
                continue
            if number == secret_number:
                print("You win!")
                break
        else:
            print("It's not an integer!")
    except ValueError:
        # Handle non-numeric input
        print("It's not a number!")