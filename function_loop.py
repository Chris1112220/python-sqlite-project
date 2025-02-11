def add_until_single_digit(num):
    while num >= 10:  # Keep looping until the number is a single digit
        num = sum(int(digit) for digit in str(num))  # Break into digits and sum them
        print(num)
    return num
      

print("Welcome to the function Loop")
user_answer = input("Please Enter a number: \n")
num = int(user_answer)
print(user_answer + " is the number you entered")
add_until_single_digit(num)


