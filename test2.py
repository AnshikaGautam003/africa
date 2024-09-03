name=input("please enter your name:")
print(f"hello {name}")
message=''' welcome to the ABC bank services.
how can i help you ?
please choose one option from the following:
option 1. CHECK BALANCE
option 2. DEPOSIT 
option 3. WITHDRAWL
'''
print(message)
task=int(input("please enter the option:"))
avalaible_amount=8000
if task>=1 and task<=3:
    print("welcome to our services!")
    if task==1:
        print("your available balance is",avalaible_amount)
        print("thank you for visiting us!")
    elif task==2:
        deposit_amount=int(input("please enter the amount that you have to deposit:"))
        if deposit_amount >= 1000:
         avalaible_amount += deposit_amount
         print(f"you have successfully deposited the amount {deposit_amount}")
         print(f"thank you for visiting us. your available balance is {avalaible_amount}")
        else:
           print("please deposit more than 1000 rupees")
    else:
        withdrawl_amount= int(input("please enter the amount that you have to withdrawl:"))
        if withdrawl_amount <= avalaible_amount:
            if withdrawl_amount > 200:
               avalaible_amount -=withdrawl_amount
               print("you have succcessfully withdrawl the amount",withdrawl_amount)
               print("thank you for visiting our site your available balance is ", avalaible_amount)
            else:
               print("insufficient balance")
else:
    print("please enter a valid option!!")
