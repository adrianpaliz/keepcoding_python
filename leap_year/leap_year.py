print("Enter the year for ckeck if is leap")

year = int(input("> "))

def is_leap(year):
    if year / 4 == int(year / 4):
        if year / 400 == int(year / 400):
            return True
            if year / 100 == int(year / 100):
                return False

print(is_leap(year))
