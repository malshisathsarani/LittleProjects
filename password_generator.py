import random

chars = "123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ<>:;,.?"
print()
print()
print()
print()
print(" _____________________________WELCOME TO PASSWORD GENARATOR_____________________" )
print()
print()
user_name =  str(input("enter your name please....? : "))
print()
print()
print(".....................................................")
print()
print()
print( "Hi....", user_name )
print()
print()
print(".....................................................")
print()
print()
user_passwords = int(input("How many passwords do you want to create : "))
user_p_length = int(input("enter password length you want : "))
print()
print()

print("here is your passwsords")

for pwd in range(user_passwords):
    mypasswords = ''
    for mypwd in range(user_p_length):
        mypasswords += random.choice(chars)
    print(mypasswords)

