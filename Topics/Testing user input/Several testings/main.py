def check(number):
    try:
        number = int(number)
        print(number if number >= 202 else "There are less than 202 apples! You cheated me!")
    except ValueError:
        print("It is not a number!")
