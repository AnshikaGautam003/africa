name=(input("PLEASE ENTER YOUR NAME:"))
print(f"HELLO,{name.upper()} WELCOME TO THE ATM SIMULATOR")
print("How May I Help You!!")
message="""please select from the following options:
1. CHECK BALANCE
2. WITHDRAWL
3. DEPOSIT
"""
print(message)

task=int(input("ENTER YOUR OPTION:"))

amount=50000   #avalaible balance default

if task>=1 and task<=3:
    #check balance program
    if task==1:
        print("Your AVALAIBLE BALANCE IS ",amount)
        print("THANK YOU FOR VISITING OUR BANK!!")
   #withdrawl program
    elif task==2:
        withdrawl_amount= int(input("PLEASE ENTER THE AMOUNT THAT YOU HAVE TO WITHDRAWL:"))
        if withdrawl_amount <= amount:
            if withdrawl_amount > 300:
                amount -= withdrawl_amount
                print("YOU HAVE SUCCESSFULLY WITHDRAWL THE AMOUNT",withdrawl_amount)
                print("THANK YOU FOR VISITING US. YOUR AVALAIBLE BALANCE IS ",amount)
            else:
                print(" PLEASE ENTER A VALID AMOUNT")
        else:
            print("INSUFFICIENT BALANCE!!")
            print("YOUR ACCOUNT DOESN'T HAVE THIS AMOUNT!! THANK YOU VISITING !!")
                
    else:
        #deposit amount program
        deposit_amount=int(input("PLEASE ENTER THE AMOUNT THAT YOU HAVE TO DEPOSIT:"))
        if deposit_amount > 1000:
            amount += deposit_amount
            print("YOU HAVE SUCCESSFULLY DEPOSITED THE AMOUNT",deposit_amount)  
            print("THANK YOU FOR VISITING OUR BANK !! YOUR AVALAIBLE BALANCE IS",amount)  
        else:
            print("PLEASE DEPOSIT MORE THAN 1000 RUPEES!!")
else:
    print("PLEASE SELECT A VALID OPTION!!")    