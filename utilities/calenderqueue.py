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

