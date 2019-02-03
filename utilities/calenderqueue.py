
"""Calender using Queue Program
This program is used to take month and year from user and print corresponding Calender using queue
Author:Laxman Raikar
Since:
    16 JAN,2019
"""

from utilities.utility import calen_queue


def calenderque():
    calen=calen_queue()
    try:
        month=int(input("enter the month :"))
    except Exception as e:
        print(e)
        print("enter integers only")
    try:
        year=int(input("enter the year :"))
    except Exception as e:
        print(e)
        print('enter integers only')

    calen.calender(month, year)


if __name__== "__main__":
    calenderque()
