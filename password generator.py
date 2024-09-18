import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("welcome to the password generator \n")
l=int(input("how many letters do you prefer:"))
no=int(input("how many numbers do you prefer "))
sy=int(input("how many symbols do you prefer "))   
password_list=[]

for char in range(0,l) :
    password_list.append(random.choice(letters))
for char in range(0,no):
    password_list.append(random.choice(numbers))
for char in range(0,sy):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(f"this is ur required password : {password}")