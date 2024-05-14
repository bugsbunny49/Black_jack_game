import random as rnd
bnk1 = rnd.randint(1,10)
bnk2 = rnd.randint(1,10)
bnk3 = rnd.randint(1,10)
bnk4 = rnd.randint(1,10)
bnk5 = rnd.randint(1,10)
bnk = bnk1+bnk2+bnk3

usr1 = rnd.randint(1,10)
usr2 = rnd.randint(1,10)
usr3 = rnd.randint(1,10)
usr = usr1+usr2

while bnk <=12:
    print("Bank take one card...")
    bnk += bnk4
    if bnk <=15:
        print("Bank take another card...")
        bnk += bnk5
    elif bnk > 21:
        print("Bank number is: ", bnk)
        print("Bank was Busted...You Win!!!")
        break
else:
    print("Your cards are: ", usr1,"|", usr2,"=",usr)
    user = input("(H)it or (R)un: ")
    if user.upper() == "H":
        user_num = int(usr+usr3)
    else:
        user_num = int(usr+0)
    if user_num > 21:
            print("Your cards are: ", usr1,"|", usr2,"=",user_num)
            print("You Busted...")
    elif bnk > 21:
            print("Bank cards are: ", bnk1, "|", bnk2, "|",bnk3,"=", bnk)
            print("Bank was Busted...You Win!!!")
    elif user_num > bnk:
            print("Your cards are: ", usr1,"|", usr2,"=",user_num)
            print( "Bank cards are: ", bnk1,"|",bnk2,"|",bnk3,"=",bnk)
            print("You Win!!!")
    else:
            print("Your cards are: ", usr1,"|", usr2,"=",user_num)
            print( "Bank cards are: ", bnk1,"|",bnk2,"|",bnk3,"=",bnk)
            print("You lose...")

#Created by Chan Myae in 27th April 2024...









