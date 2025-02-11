import greeting
import sys


greeting.welcome()

def prime_number_finder():
    num = int(input("Please enter a number: \n"))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
    return num

print("Welcome to the function Loop")

prime_number_finder()