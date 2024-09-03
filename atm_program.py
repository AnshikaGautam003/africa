name = input("Plz enter your name : ")
print(f"Hello {name}!") 
message = """
How may i help you sir .

Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL.
"""
print(message) 
task = int(input("Plz enter your option : "))
available_amount = 5000
if task >=1 and task <=3:
    print("welcome to yuo in virtual bank program!")

    # check balance  
    if task == 1:
        print("Thank you for using our service your current balance is : ",available_amount) 

#  deposit progrma
    elif task == 2:
        deposit_amount = int(input('plz enter deposit amount : '))  # 6000,
        if deposit_amount >= 500:
            available_amount += deposit_amount
            print("You have successfully deposited your amount is : ",deposit_amount)
            print("Thank you for using our service your current balance is : ",available_amount) 
        else:

            print("plz deposit more than 500 rupess!")



# withdrawl progr.
    else:
        withdrawl_amount= int(input("please enter the amount that you have to withdrawl:"))
        if withdrawl_amount <= available_amount:
           if withdrawl_amount > 200:
               available_amount -=withdrawl_amount
               print("you have succcessfully withdrawl the amount",withdrawl_amount)
               print("thank you for visiting our site your available balance is ", available_amount)
        else:
            print("insufficient balance")

                

else:
    print("plz choose in btwn 1 to 3")
