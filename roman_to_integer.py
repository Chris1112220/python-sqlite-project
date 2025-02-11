def roman_to_int(str):
    roman_dictionary = { "I": 1,
                     "V": 5,
                     "X": 10,
                     "L": 50,
                     "C": 100,
                     "D": 500,
                     "M": 1000
                     }
    result = 0 

    for i in range(len(str)):
        if i < len(str) - 1 and roman_dictionary[str[i]] < roman_dictionary[str[i + 1]]:
            result -= roman_dictionary[str[i]]
        else:
            result += roman_dictionary[str[i]]

    return result



print("Welcome to Roman to Integer")
answer = input("Please enter a Roman Numberal and it will be converted to a number \n")
print(answer)
print(roman_to_int(answer))

