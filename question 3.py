# question number 3
import math

print("Welcome to the Old College Bookstore!")
print(" ")

Y = True

while Y == True:
   price = float(input("What is the price of the book?"))
   quantity = float(input("How many books will be ordered?"))
   tax = float(price * quantity * 0.095)
   shipping = float(price * quantity + 3)
   total = float(price * quantity + tax + shipping)
   print(f"The total is {total}")
   more = input("Any more books? (Y/N)")
   if more == "Y" or more == "y":
     continue
   else:
     break
print ("Have a good day!")