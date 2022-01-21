print("Enter the year for ckeck if is leap")
year = int(input("> "))

def is_leap(year):
    if (year / 4) ==  int(year / 4):
        if (year / 100) == int(year / 100):
            if (year / 400) == int(year / 400):
                print("The year {} is leap.".format(year))
            else:
                print("The year {} is not leap.".format(year))
        else:
            print("The year {} is leap.".format(year))
    else:
        print("The year {} is not leap.".format(year))

is_leap(year)
