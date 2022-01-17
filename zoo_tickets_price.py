def ticket_price_calculation(age):
    if age > 0 and age <= 2:
        price = 0
    elif age <= 12:
        price = 14
    elif age < 65:
        price = 23
    else:
        price = 18
    return price

def age_imput():
    age = input("How old you are?: ")
    age = int(age)
    return age

age = age_imput()

total_price = 0

while age != 0:
    ticket_price = ticket_price_calculation(age)
    print("Ticket price: {}".format(ticket_price))
    total_price += ticket_price

    age = age_imput()

print("Total: {}".format(total_price))