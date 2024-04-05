#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters1 = ""
for i in range(0, nr_letters):
    letters1 += str(letters[random.randint(0, len(letters) - 1)])
#print(letters1)
symbols1 = ""
for i in range(0, nr_symbols):
    symbols1 += str(symbols[random.randint(0, len(symbols) - 1)])
#print(symbols1)
numbers1 = ""
for i in range(0, nr_numbers):
    numbers1 += str(numbers[random.randint(0, len(numbers) - 1)])
#print(numbers1)
password = letters1 + symbols1 + numbers1
#print(password)
password_list = list(password)
random.shuffle(password_list)

shuffled_pass = ''.join(password_list)
print("Here is your password: " + shuffled_pass)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
