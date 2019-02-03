"""this program is used to  load inventory Data Management of Rice, Pulses and Wheats
    from json file and append the items of rice,pulses and wheats from user
    author:Laxman Raikar
    since:28 JAN,2019
"""
import json


class InventoryAdd:
    @staticmethod
    def order():
        try:
            with open("by.json","r" ) as f:
                data = json.load(f)
                # loading the json data into the variable
        except FileNotFoundError:
            print("not found")
            exit()
            # if file not found it will exit out
        print("Available items in our grocery store:")

        print("rice :")
        for r in data["rice"]:
            print(r['name'], "- Per kg", r['price'], "Available-", r['available'], "kg")
            # printing the rice details

        print("Pulses :")
        for p in data['pulses']:
            print(p['name'], "- Per kg", p['price'], "Available-", p['available'], "kg")
            # printing the pulse details

        print("Wheats :")
        for w in data['wheats']:
            print(w['name'], "- Per kg", w['price'], "Available-", w['available'], "kg")
            # printing the wheat details

        print("")
        i = input("rice or pulses or wheats\n")
        try:
            if i == 'rice' or i == 'pulses' or i == 'wheats':
                pass
            else:
                raise ValueError
        except ValueError:
            print("invalid input")
            exit()
        item_name = input("item name :")
        price = int(input("price :"))
        available = int(input("quantity :"))

        with open("by.json", 'r') as f:
            str = f.read()
            obj = json.loads(str)

        with open("by.json", 'w') as f:
            obj[i].append({
                "name": item_name,
                "price": price,
                "available": available
            })
            f.write(json.dumps(obj, indent=1))
            f.close()


if __name__ == "__main__":
    I = InventoryAdd()
    I.order()