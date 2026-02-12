'''Which bin is it'''
'''This program tracks what bin do i have to take out'''
'''12/02/2026'''

# def user_input():
#     date = int(input("What week is it, (1-52), must be interger: "))
#     return date

def time_checker():
    import datetime
    x = datetime.datetime.now()
    x = int(x.strftime("%V"))
    return x 

def checker(date):
    if date < 1 or date > 52:
        return "There are onyly 52 weeks in a year"
    elif date % 2 == 0:
        return "Green and Red bins"
    elif date % 2 == 1:
        return "Green and Yellow bins"
    else:
        return "none"

def main():
    print("This program tells you which bins, you should take out")
#     a = user_input()
    b = time_checker()
    print(checker(b)) # replace b with a for manual
    print("End of program")
main()
