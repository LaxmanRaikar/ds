import json
import datetime
from utilities.utility import que

que_obj = que


class CommercialQueue:

    try:
        def __init__(self):
            with open("stock.json", "r") as stock_json_file:
                stock_json_file = json.load(stock_json_file)      # load() convert file into python from json

            self.stock_jf = stock_json_file
            with open("customer.json", "r") as person_json_value:
                person_json_value = json.load(person_json_value)
            self.person_json_value = person_json_value

        def view_shares(self):                   # Iterating through Stock Report by means of checking the length
            for share in range(len(self.stock_jf['company'])):
                print(share, self.stock_jf['company'][share])

        def check_validity(self):
            number = 0
            name = input("Enter Username\n")
            # while number < len(self.person_json_value["Person"]):  # Creating the user for buying or selling a shares
            #  if self.person_json_value["Person"][number]["Name"] == name.title():  # Verifying the user
            index = number
            print(self.person_json_value["Person"][number])
            print("....Login successful....")
            read_input2 = int(input("1:Buy shares\n2:Sell shares:\n"))
            if read_input2 == 1:
                commercial_object.buy_share(index, name)
            elif read_input2 == 2:
                commercial_object.sell_share(index, name)

            else:
                print("wrong Input")

            number += 1

        def add_new_company(self):                               # Add a new company by adding a new through dictionary
            name = input("Enter company name\n")
            number = int(input("Enter Your Number of share\n"))
            price = int(input('Enter Your Price per share\n'))
            new_stock_dict = {"name": name,                 # created the dictionary for a new values

                              "share": number,

                              "price": price}
            try:
                with open("stock.json", 'w') as stock_jf:                # Add a new file in a json through a key
                    self.stock_jf['company'].append(new_stock_dict)
                    stock_jf.write(json.dumps(self.stock_jf, indent=2))  # Writing a file through python to json

            except FileNotFoundError:
                print("File Not Found")

        def buy_share(self, index, name):
            for bu_share in range(len(self.stock_jf['company'])):
                print(bu_share, self.stock_jf['company'][bu_share])

            print('Enter Which Company Share you want to buy\n')
            choice = int(input("Enter choice in Int\n"))
            buy_share = int(input("Enter Number of Share You want to buy\n"))
            each_share_price = self.stock_jf['company'][choice]['price']
            # Asking for a user to sell shares among indexing
            amount_pay = buy_share * each_share_price     # Calculating the share that are purchasing

            if self.person_json_value['Person'][index]["Total Balance"] > amount_pay:
                # Balance should be there while purchasing
                print("Total amount you have to pay for ", buy_share, " stocks : ", amount_pay)
                updated_stock_share = self.stock_jf["company"][choice]["share"] - buy_share
                # Updating the stock

                with open("stock.json", "w") as jf:  # Changing the updated stock in a file
                    self.stock_jf["company"][choice]["share"] = updated_stock_share
                    jf.write(json.dumps(self.stock_jf, indent=2))

                person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
                # Subtracting the new share amount from a balance
                print('Now Your Updated Balance is ', person_updated_balance)
                person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share
                # Adding the new shares in a stock
                print('Now Your Updated Number of share is ', person_updated_share, "\n")
                dt = datetime.datetime.now()                             # to show the date

                que_obj.queue( self.stock_jf["company"][choice]["name"],  buy_share)

                with open("transaction.txt", "a")as txt:          # open file to append data
                    txt.write(name + str(que_obj.show()) + str(dt) + "\n")
                print("stack show")
                que_obj.show()

                que_obj.show()

                with open("customer.json", "w") as jf:                  # open a file to write data
                    self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                    self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                    jf.write(json.dumps(self.person_json_value))
            else:
                print("You Don't have enough money ")

        def sell_share(self, index, name):
            print('Enter choice to sell your share to particular company\n')

            # this loop is used to show the share of shock report
            for share in range(len(self.stock_jf['company'])):
                print(share, self.stock_jf['company'][share])

            choice = int(input("Enter choice in Int\n"))

            print('Enter Number of share you want to sell to', self.stock_jf['company'][choice]['name'],
                  'company', "\n")
            sell_share = int(input("Number of shares to sell \n"))
            updated_stock_share = self.stock_jf["company"][choice]["share"] + sell_share

            with open("stock.json", "w") as jf:     # open a file to dump data (python to json)
                self.stock_jf["company"][choice]["share"] = updated_stock_share
                jf.write(json.dumps(self.stock_jf, indent=2))
            # updated share of a person
            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share

            person_share_price = int(input("price for per share you want from company\n"))
            # user updated balance
            person_updated_balance = self.person_json_value['Person'][index][
                                         "Total Balance"] + person_share_price * sell_share

            print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance')
            print('Now Your Updated Balance is ', person_updated_balance, "\n")

            print('Now Your Updated Number of share is ', updated_person_share, "\n")
            # add the stock report in the inventory
            que_obj.queue((self.stock_jf["company"][choice]["name"],"Number of shares :", sell_share))
            print("stack show")
            que_obj.show()

            que_obj.show()

            with open("customer.json", "w") as jf:                  # open file to write the user details
                self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                jf.write(json.dumps(self.person_json_value, indent=2))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    while True:
        commercial_object = CommercialQueue()                       # object for person class
        commercial_object.view_shares()
        print("\n")
        try:
            read_input = int(input("1: Admin Login or 2: User \n"))
            if read_input == 1:                                  # To enter as admin
                print("welcome Admin")
                read_input1 = int(input("1 to add Company :\n"))
                if read_input1 == 1:
                    commercial_object.add_new_company()
            elif read_input == 2:                                # To enter as user
                print("Welcome User")
                commercial_object.check_validity()

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid Value")