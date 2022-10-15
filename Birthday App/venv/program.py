import datetime


def print_header():
    print('-------------------------')
    print('     birthday app')
    print('-------------------------')
    print()


def get_birthday_from_user():
    print("When were you born?")

    try:
        year = int(input("Year [YYYY]: "))
    except ValueError:
        print("Please enter a number")
        get_birthday_from_user()

    try:
        month = int(input("Month [MM]: "))
    except ValueError:
        print("Please enter a number")
        get_birthday_from_user()

    try:
        day = int(input("Day [DD]: "))
    except ValueError:
        print("Please enter a number")
        get_birthday_from_user()

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date): 
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print("You had your birthday {} days ago this year.".format(-days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("Happy Birthday")


def try_again():
    print("do you want to try again?")
    ch = None
    ch = input("[Y]es or [N]o: ")
    if ch == 'y':
       main()
    elif ch == 'n':
        print('goodbye')
    else:
        print('wrong input')
        try_again()



def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)
    try_again()

main()
