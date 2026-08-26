def check_even_odd(num):
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

def check_positive_negative(num):
    if num > 0:
        print("The number is Positive")
    elif num < 0:
        print("The number is Negative")
    else:
        print("The number is Zero")

num = 10

check_even_odd(num)
check_positive_negative(num)