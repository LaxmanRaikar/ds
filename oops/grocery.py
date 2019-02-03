"""this program is used to  load inventory Data Management of Rice, Pulses and Wheats
    from json file
    author:Laxman Raikar
    since:28 JAN,2019
"""
import json


class Grocery:

    def __init__(self):
        try:
            with open("by.json", "r") as f:
                data = json.load(f)
                # load() convert json file to python
                # if file not found it will throw error
        except FileNotFoundError:
            print("File not found...please check path")
            exit()
        self.data = data

    def inventory(self):
        rice={}
        #  taking dictionary to store the key and values and finally print the total
        for r in self.data["rice"]:
            rice_name= r['name']            # storing the name of rice item
            rice_price = r['price']      # storing price of rice item
            rice[rice_name] = rice_price    # adding price and name to the dictionary
        print("rice details:", rice)
        print("Total rice items are:", len(rice))
        print("Total price of rice: ", sum(rice.values())) # sum will add the all values present in the dictionary

        pulse = {}
        # taking dictionary to store the key and values and finally print the total
        for p in self.data["pulses"]:
            pulse_name= p["name"]       # storing the name of pulse item
            pulse_price = p["price"]    # storing the price of pulse item
            pulse[pulse_name] = pulse_price

        print("pulse details:", pulse)
        print("Total pulse items are:", len(pulse))
        print(sum(pulse.values()))      # sum will add the all values present in the dictionary

        wheat = {}
        # taking dictionary to store the key and values and finally print the total
        for w in self.data["wheats"]:
            wheat_name = w["name"]      # storing the wheat item name
            wheat_price = w["price"]    # storing the wheat item price

            wheat[wheat_name] = wheat_price     # adding to the dictionary

        print("wheat details:", wheat)
        print("Total wheat items are:", len(wheat))
        print("", sum(wheat.values()))          # sum will add the all values present in the dictionary


if __name__ == "__main__":
    g = Grocery()
    g.inventory()