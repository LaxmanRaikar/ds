from utilities.utility import que
s=que()
try:
    no_of_people=int(input("enter the number of people in queue :"))

except ValueError:
    print("enter the decimal value")

for i in range(0,no_of_people):
    print(s.queue(i))
