
    
#-----------------------get a random choice-------------------------------------
    
import random

random_choice = ["rock", "paper" ,"sissor"]
random_choice = random.sample(random_choice,1)


# ----------------------------------------welcome to user------------------
user_name = str(input("enter your name player....  "))
print()
print()
#print("HI___",user_name,"WELCOME to rock sissor paper game '_'   ")
print()
print()
#user_ask = str(input(" ARE YOU READY ?   :"))
#user_ask = "yes"
print( "LET'S GO BUDDY.......  " )
print()
print()

#------------------------give a attempt limit---------------------------------

attempt = 0
while(attempt < 2 ):
    
#--------------------get a user choice--------------------------------------


    user_choice = str(input("enter your choice.....rock, paper or sissor?? :  "))

#------------------------------------compare with random import--------------------------


    if random_choice[0] == user_choice :
        print("///GAME END//// both players selected", user_choice, "You are drow!!!")
        break





    if random_choice[0] == "rock" :
        if user_choice == "paper" :
            print(user_name,"YOU WON!!!  ")
        else :
            print("you lose... rock samash sissor  ")
    elif random_choice[0]  == "paper" :
        if user_choice == "sissor" :
            print(user_name, "..YOU WON !!!")
        else: 
            print("you lose... paper cover rock  ")
    elif random_choice[0]  == "sissor" :
        if user_choice == "rock" :
            print(user_name, "..YOU WON !!!")
        else:
            print("you lose... sissor cut paper] ")


    attempt = attempt + 1



            
    
else:
    print("your attempts are over.. thank you")
    
again =str(input("Do you want play again(yes/no)? "))



