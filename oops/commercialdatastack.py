import json
import datetime
from utilities.utility import Stack


s = Stack()



class DataQueue:
    try:
        def __init__(self):
            with open("stock.json", "r") as stock_jf:
                stock_jf = json.load(stock_jf)  # load() convert file into python from json

            self.stock_jf = stock_jf
            with open("customer.json", "r") as person_json_value:
                person_json_value = json.load(person_json_value)  # load() convert file into python from json
            self.person_json_value = person_json_value

        def view_shares(self):
            # this method is used to print the company name and their stock details
            for i in range(len(self.stock_jf['company'])):
                print(i, self.stock_jf['company'][i])

        def check_validity(self):
            # this method is used to validate the user login and to buy or sell share

            print("*********** Welcome **************")
            i = 0
            name = input("Enter Username")
            while i < len(self.person_json_value["Person"]):
                if self.person_json_value["Person"][i]["Name"] == name.title():
                    index = i
                    print(self.person_json_value["Person"][i])
                    print("....Login successful....")
                    while True:
                        try:
                            c = int(input("1:Buy shares\n2:Sell shares:"))
                            break
                        except ValueError:
                            print("enter the decimal value")
                    if c == 1:
                        self.buy_share(index, name)
                    elif c == 2:
                        self.sell_share(index, name)

                    else:
                        print("wrong Input")
                i += 1

        def add_new_company(self):
            # this method is used to add company details into the json file
            name = input("Enter company name")
            number = int(input("Enter Your Number of share"))
            price = int(input('Enter Your Price per share'))
            new_stock_dict = {"name": name,

                              "share": number,

                              "price": price}

            with open('stock.json', 'w') as stock_jf:
                self.stock_jf['company'].append(new_stock_dict)

                stock_jf.write(json.dumps(self.stock_jf, indent=2))
                # adding the details to json file after converting from python to json

        def buy_share(self, index, name):
            for i in range(len(self.stock_jf['company'])):
                print(i, self.stock_jf['company'][i])
                # print the stock details of company
            print('Enter Which Company Share you want to buy')
            choice = int(input("Enter choice in Int"))
            buy_share = int(input("Enter Number of Share You want to buy"))
            each_share_price = self.stock_jf['company'][choice]['price']
            amount_pay = buy_share * each_share_price   # calculate the total of purchased share

            if self.person_json_value['Person'][index]["Total Balance"] > amount_pay:

                print("Total amount you have to pay for ", buy_share, " stocks : ", amount_pay )
                updated_stock_share = self.stock_jf["company"][choice]["share"] - buy_share
                with open("stock.json", "w") as jf:
                    self.stock_jf["company"][choice]["share"] = updated_stock_share
                    jf.write(json.dumps(self.stock_jf, indent=2))

                person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
                print('Now Your Updated Balance is ', person_updated_balance)
                person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share
                print('Now Your Updated Number of share is ', person_updated_share)
                dt = datetime.datetime.now()

                s.push(("Buy", self.stock_jf["company"][choice]["name"],"shares : ",buy_share))
                with open("transaction.txt", "a")as txt:
                    txt.write(name+str(s.show())+str(dt)+"\n")
                print("stack show")
                s.show()

                with open("customer.json", "w") as jf:
                    self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                    self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                    jf.write(json.dumps(self.person_json_value))

            else:
                print("You Don't have enough money ")

        def sell_share(self, index, name):
            print('Enter choice to sell your share to particular company')
            for i in range(len(self.stock_jf['company'])):
                print(i, self.stock_jf['company'][i])

            choice = int(input("Enter choice in Int"))

            print('Enter Number of share you want to sell to', self.stock_jf['company'][choice]['name'],
                  'company')
            sell_share = int(input("Number of shares to sell "))
            updated_stock_share = self.stock_jf["company"][choice]["share"] + sell_share
            with open("stock.json", "w") as jf:
                self.stock_jf["company"][choice]["share"] = updated_stock_share
                jf.write(json.dumps(self.stock_jf, indent=2))

            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share

            person_share_price = int(input("price for per share you want from company"))
            person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] + person_share_price * sell_share

            print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance')
            print('Now Your Updated Balance is ', person_updated_balance)

            print('Now Your Updated Number of share is ', updated_person_share)

            st = datetime.datetime.now()

            s.push(("Sold", self.stock_jf["company"][choice]["name"],"Number of shares : ",sell_share))
            with open("transaction.txt", "w")as txt:
                txt.write(name + str(s.show()) + str(st) + "\n")
            print("stack show")
            s.show()

            with open("customer.json", "w") as jf:
                self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                jf.write(json.dumps(self.person_json_value, indent=2))

    except Exception as e:
        print(e)


def customer_data():
    p = DataQueue()
    p.view_shares()
    # calls view share method

    print("\n1.Admin login.\n2.User login.\n3.Exit ")
    while True:
        try:

            choice = int(input("\nEnter choice:"))
            break
        except ValueError:
            print("enter the decimal value")
            continue

    if choice == 1:
        print("\nwelcome Admin")
        print("\n1.To add Company\n2.Exit")
        while True:
            try:
                j = int(input("Enter choice:"))
                break
            except ValueError:
                print("enter the decimal value")
                continue
        if j == 1:
            p.add_new_company()
            # calls add_new_company() method
            p.view_shares()
            # calls view shares method
        elif j == 2:
            exit(0)
        else:
            print("you have entered wrong input..")
    elif choice == 2:
        print("Welcome User")
        p.check_validity()
        # calls check_validity method
    elif choice == 3:
        exit(0)
    else:
        print("Invalid choice....")


if __name__ == "__main__":
    customer_data()