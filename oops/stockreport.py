import json

json_data = open("stock.json").read()
data = json.loads(json_data)     # loading the json data into the variable

count=1                     # intialization
list = []                     # empty list
print(" ino","company name", "  price per share")
for i in data["company"]:               # loop to print the company name and price of shares
    print(" ", count, " ", i["name"], "\t\t\t\t", i["price"],)
    count+=1
print("\n")
print("****************************************************************************")
no_companies_shares=int(input("enter the total number of companies whose "
                              "shares you want to purchase:\n"))
print("............................................................................")
for j in range(no_companies_shares):    # loop for n number of companies which user needs
    company_index_number=int(input("enter the index number of company :\n"))-1
    key=data["company"][company_index_number]
    """here we are pointing to the index number of sub keys which is present in key of json file """
    no_shares=int(input("enter the number of shares\n"))
    total=key["price"]*no_shares  # calculating the price of share with number of shares given from user
    print("total price of selected company share",total,"Rs"
                                                        "")
    print("***************************************************************************")
    list.append(total)   # appending the total value in the list so that we can calculate the total price
sum = 0        #intialization
for k in range(0,len(list)):        # loop to calculate the sum of elements in list
    sum = sum+list[k]
print("final total",sum,"Rs")