from utilities.utility import calenarray
def calender_queue_runner():

    logic_obj =calenarray()

    try:
        month = int(input('Enter Month:'))
    except Exception as e:
        print(e)
        print("Enter integer only ")
    try:
        year = int(input('Enter year:'))
    except Exception as e:
        print(e)
        print("Enter integer only")

    logic_obj.calender(month, year)


if __name__ == "__main__":
    calender_queue_runner()