"""this program is used to add the company details using linked list
author:Laxman Raikar
since:28 JAN,2019"""

import json
from utilities.utility import LinkedList

linked_list_object = LinkedList()  # object of the class
try:
    with open("stock.json", "r") as sf:
        stock = json.load(sf)     # loading to python from json
except FileNotFoundError:
    print("File not Found")
    exit()
for i in stock['company']:
    linked_list_object.append(i)            # adding the values to the linked list
print(linked_list_object.display())         # printing the values from linked list

name = input("name :")                      # entering the details of company
number = int(input("numbers :"))
price = int(input("price :"))

add = {
      "name": name,
      "share": number,
      "price": price
}

linked_list_object.append(add)              # adding the company details to the linked list

print(linked_list_object.display())         # displaying linked list values

add_stock = {"company": []}
for item in linked_list_object.display():
    add_stock["company"].append(item)

with open("stock.json", "w") as f:
    data = json.dumps(add_stock, indent=2)   # adding value to the json file
    f.write(data)

