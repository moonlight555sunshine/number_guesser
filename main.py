import random
secret_number = random.randint(1, 101)
while True:
    number = input("Guess the number: ")
    try:
        number = float(number)
        if number.is_integer():
            if number < 0 or number > 100:
                print("It's not in range 0-100!")
                continue
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
        print("It's not a number!")