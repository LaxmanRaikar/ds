"""Calender Program
This program is used to take month and year from user and print corresponding Calender
Author:Laxman Raikar
Since:
    16 JAN,2019
"""

from utilities.utility import calenarray


def calender_():

    logic_obj = calenarray()         # creating the object of class
    while True:
        try:
            month = int(input('Enter Month:'))
            break
        except ValueError:
            print("Enter integer only ")
            continue
    while True:
        try:
            year = int(input('Enter year:'))
            break
        except ValueError:
            print("Enter integer only")
            continue

    logic_obj.calender(month, year)         # calling the class and passing parameters


if __name__ == "__main__":
    calender_()