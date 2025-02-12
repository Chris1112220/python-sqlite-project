
import math

print("Welcome to the program")



def prime():

    try:
        num = int(input("Enter a number: "))
 
    
   
        if num <= 1:
            print("Not a prime number")
            return

    except ValueError:
            print("you need to enter a number")
            return
        
  
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
        else:
            print("Prime number")



prime()