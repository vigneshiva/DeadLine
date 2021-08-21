import datetime

user_input = input("enter your goal : deadline as dd.mm.yyyy format- ").split(":")

goal = user_input[0]
deadline = user_input[1]

date_time_type = datetime.datetime.strptime(deadline, "%d.%m.%y")
today = datetime.datetime.today()

difference = date_time_type - today
days_left = int(str(date_time_type - today).split()[0])

while days_left >0:
    if days_left > 10:
        print(f"{difference.days} days left")
    elif days_left < 10:
        print(f"Hurry up, only {difference.days} days left")
    elif days_left == 1:
        print(f"Only {difference.days} more day left")
    else:
        print("Times up. hope you would have finished your task")
    break
else:
    print("enter a valid date")
