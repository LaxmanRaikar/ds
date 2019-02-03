
""" Bank Cash Counter Program
This program actually demonstrate bank cash counter where people can come for withdraw money or
user can deposit money in the bank and from the beginning itself bank cash will be maintained accordingly
Author:Laxman Raikar
Since:
    16 jan,2019
"""
from utilities.utility import que
bank_cash=20000
s = que()    # initialization

while True:
    try:
        no_of_people=int(input("enter the number of people in queue :"))
        break
    except ValueError:
        print("enter the decimal value")
        continue


for i in range(0,no_of_people):
    s.queue(i)

while bank_cash != 0 or len(s.list)>0:     # using loop to execute the code till list to empty
    print("*************************")
    print("welcome to bridgelabz bank")

    while True:
        try:
            choice=int(input("1.deposit\n2.withdraw\n"))
            break
        except ValueError:
            print("enter the decimal value")
            continue
    try:

        if choice == 1:                            # option to deposit
            deposit_amount=(int(input("enter the deposit amount  :")))
            bank_cash=bank_cash+deposit_amount     # adding deposit amount to bank cash
            print("Cash has been deposited,THANK YOU!!!")
            s.dequeue()                             # the list is decremented by 1
            print("No of people remaining in queue", s.size())

            if s.size()==0:
                print("process completed")
                break

        elif choice == 2:
            withdrawl_amount=int(input("enter the withdrawl amount \n"))

            if withdrawl_amount>bank_cash:
                print("********sorry for the inconvenience,as we dont have sufficient balance to withraw the "
                          "amount******** \n"
                          "you can withdraw the amount till", bank_cash, "rs")
                print("enter 1 to withdraw or enter 2 to close")
                withdraw_choice=int(input("enter the number :"))

                if withdraw_choice == 1:
                    draw_amount=int(input("enter the withrawl amount :"))
                    bank_cash=bank_cash-draw_amount
                    s.dequeue()
                    print("No of people remaining in queue",s.size())

                    if s.size()==0:
                        print("process completed")
                        break

                else:
                    print("Thank you")
                    exit(0)

            else:
                print("Thank you for transaction in our bank ")
                bank_cash=bank_cash-withdrawl_amount
                s.dequeue()
                print("No of people remaining in queue", s.size())

                if s.size()==0:
                    print("process completed")
                    break

        else:
            print("Enter 1 or 2")

    except  ValueError:
        print("enter the decimal value")
        break
