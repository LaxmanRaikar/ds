"""this program is used to replace the particular string with string given by user
    author:Laxman Raikar
    since:28 JAN,2019
"""

import re


def regex():
    string = 'Hello <<name>>, We have your full name as <<full name>> in our system.' \
                 '\n your contact number is 91-xxxxxxxxxx.' \
                 '\n Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2019. '

    template = ['<<name>>', '<<full name>>', 'xxxxxxxxxx', '01/01/2019']
    # user input list
    list = ['Enter Your First Name: ', 'Enter Your Full Name: ', 'Enter Your Mobile Number(10 digits only):', "Enter Today's Date[dd/mm/yyy]:"]

    for i in range(4):
        print(' =>', list[i])   # print list array elements to take input from user
        # sub() method check the pattern and replace string with pattern
        replaced_string = re.sub(template[i], str(input()), string)
        string = replaced_string
        print(string)


regex()