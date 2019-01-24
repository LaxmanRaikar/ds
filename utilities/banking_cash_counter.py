from utilities.utility import stack
bank_cash=20000
s=stack()                           #initialization
try:
    no_of_people=int(input("enter the number of people in queue :"))
except Exception as e:
    print(e)
    print("give the input in numbers only")
for i in range(1,no_of_people):
    s.queue(i)
while bank_cash != 0 or len(s.list)>0:     #using loop to execute the code till list to empty
    print("*************************")
    print("welcome to bridgelabz bank")
    choice=int(input("1.deposit\n2.withdraw\n"))
    try:
            if choice == 1:                            #option to deposit
                deposit_amount=(int(input("enter the deposit amount  :")))
                bank_cash=bank_cash+deposit_amount     #adding deposit amount to bank cash
                print("Cash has been deposited,THANK YOU!!!")
                s.dequeue()                             #the list is decremented by 1
                print("No of people remaining in queue",s.size()+1)
            elif choice == 2:
                withdrawl_amount=int(input("enter the withdrawl amount \n"))

                if withdrawl_amount>bank_cash:
                    print("********sorry for the inconvenience,as we dont have sufficient balance to withraw the amount******** \n"
                        "you can withdraw the amount till",bank_cash,"rs")
                    print("enter 1 to withdraw or enter 2 to close")
                    withdraw_choice=int(input("enter the number :"))
                    if withdraw_choice == 1:
                        draw_amount=int(input("enter the withrawl amount :"))
                        bank_cash=bank_cash-draw_amount
                        s.dequeue()
                        print("No of people remaining in queue",s.size()+1)
                    else:
                        print("Thank you")
                        exit(0)
                else:
                    print("Thank you for transaction in our bank ")
                    bank_cash=bank_cash-withdrawl_amount
                    s.dequeue()
                    print("No of people remaining in queue",s.size()+1)
            else:
                print("Enter 1 or 2")
    except Exception as e:
        print("counter closed ")
        break
