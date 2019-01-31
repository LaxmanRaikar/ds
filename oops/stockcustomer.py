import json
class Accounts:
        def __init__(self):
            with open("stock.json", "r") as stock_jf:
                stock_jf = json.load(stock_jf)  # load() convert file into python from json
            self.stock_jf = stock_jf
            with open("customer.json", "r") as person_json_value:
                person_json_value = json.load(person_json_value)  # read customer json file
            self.person_json_value = person_json_value

        def view_shares(self):
            #to print the  shares this method is used

            for i in range(len(self.stock_jf['company'])):
                print(i, self.stock_jf['company'][i])
            print("************************************************")

        def check_validity(self):


            print("*********** Welcome **************")
            i = 0
            name = input("Enter Username :")
            while i < len(self.person_json_value["Person"]):
                # title() method returns a copy of the string in which
                # first characters of all the words are capitalized.
                if self.person_json_value["Person"][i]["Name"] == name.title():
                    index = i
                    print(self.person_json_value["Person"][i])  # print all data of customer
                    print("....Login successful....")

                    # provide options
                    c = int(input("1.Buy shares\n2.Sell shares\n3.Exit"))
                    if c == 1:
                        self.buy_share(index)  # for buying shares
                    elif c == 2:
                        self.sell_share(index)  # for selling shares
                    elif c == 3:
                        exit(0)
                    else:
                        # in case of user entered wrong input display following message
                        print("wrong Input")
                i += 1

        def add_new_company(self):


            print("**************************************")
            name = input("Enter company name: ")
            number = int(input("Enter Number of share: "))
            price = int(input('Enter Price per share: '))
            new_stock_dict = {"name": name,  # add at new index in stock report
                              "share": number,
                              "price": price}

            with open('stock.json', 'w') as stock_jf:
                self.stock_jf['company'].append(new_stock_dict)  # append updated data into stocks
                stock_jf.write(json.dumps(self.stock_jf, indent=2))
        def buy_share(self, index):

            for i in range(len(self.stock_jf['company'])):
                print(i, self.stock_jf['company'][i])  # print stock data

            # taking input from user
            print('\nEnter Which Company Share you want to buy')
            choice = int(input("Enter company index number: "))
            buy_share = int(input("Enter Number of Share You want to buy: "))
            each_share_price = self.stock_jf['company'][choice]['share']
            amount_pay = buy_share * each_share_price  # calculate total purchased share price

            # checks balance before purchase. if balance enough then proceed else terminate
            if self.person_json_value['Person'][index]["Total Balance"] > amount_pay:

                print("Total amount you have to pay for ", buy_share, " stocks :", amount_pay)
                updated_stock_share = self.stock_jf["company"][choice]["share"] - buy_share

                # update stocks after purchasing
                with open("stock.json", "w") as jf:
                    self.stock_jf["company"][choice]["share"] = updated_stock_share
                    jf.write(json.dumps(self.stock_jf, indent=2))

                person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
                print('Now Your Updated Balance is ', person_updated_balance)
                person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share
                print('Now Your Updated Number of share is ', person_updated_share)

                # update customer data also
                with open("customer.json", "w") as jf:
                    self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                    self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                    jf.write(json.dumps(self.person_json_value))
            else:

                # if customer don't have enough balance then print following message
                print("You Don't have enough money ")

        def sell_share(self, index):


            print('Enter choice to sell your share to particular company')
            for i in range(len(self.stock_jf['company'])):
                print(i, self.stock_jf['company'][i])  # print stock report

            choice = int(input("Enter choice (company index): "))

            print('Enter Number of share you want to sell to', self.stock_jf['company'][choice]['name'],
                  'company')
            sell_share = int(input("Number of shares to sell: "))
            updated_stock_share = self.stock_jf["company"][choice]["share"] + sell_share

            # update stock report data
            with open("stock.json", "w") as jf:
                self.stock_jf["company"][choice]["share"] = updated_stock_share
                jf.write(json.dumps(self.stock_jf, indent=2))  # write updated data into stock report

            # calculate updated person shares
            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share

            person_share_price = int(input("price for per share you want from company"))
            person_updated_balance = self.person_json_value['Person'][index][
                                         "Total Balance"] + person_share_price * sell_share
            # print all transaction data
            print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance')
            print('Now Your Updated Balance is ', person_updated_balance)

            print('Now Your Updated Number of share is ', updated_person_share)

            # update customer data also
            with open("customer.json", "w") as jf:
                self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                jf.write(json.dumps(self.person_json_value, indent=2))
def account_runner():
    p = Accounts()
    p.view_shares()

    print("\n1.Admin login.\n2.User login.\n3.Exit ")
    choice = int(input("\nEnter choice:"))
    if choice == 1:
        print("\nwelcome Admin")
        print("\n1.To add Company\n2.Exit")
        j = int(input("Enter choice:"))
        if j == 1:
            p.add_new_company()
            p.view_shares()
        elif j == 2:
            exit(0)
        else:
            print("you have entered wrong input..")
    elif choice == 2:
        print("Welcome User")
        p.check_validity()
    elif choice == 3:
        exit(0)
    else:
        print("Invalid choice....")
if __name__ == "__main__":
    account_runner()

