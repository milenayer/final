flat_dict = {}
pay = 0
if_absent = 0
while True:
    user_input = input()
    if user_input[:4] == "add":
        flat_dict[user_input[11:]] = 0
    elif user_input[:4] == "set":
        if user_input[5:] == "salary":
            pass
        elif user_input[5:] == "absent":
            pay -= if_absent
        elif user_input[5:] == "rent":
            pay += int(user_input.split()[-1])
            if_absent = int(user_input.split()[-1])
        elif user_input[5:] == "bills":
            pay += int(user_input.split()[-1])
    elif user_input == "calculate":
        print(pay)
    elif user_input == "reset":
        break