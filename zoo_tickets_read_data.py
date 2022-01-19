from zoo_tickets_configuration import tickets_prices

tickets_file = open('transactions.txt', 'r')

number_tickets_baby = 0
number_tickets_kid = 0
number_tickets_adult = 0
number_tickets_senior = 0

line_transaction = tickets_file.readline()

total_tickets = 0
total_price = 0

while line_transaction != '':
    tickets = line_transaction.split(',')
    number_tickets_baby += int(tickets[0])    
    number_tickets_kid += int(tickets[1])
    number_tickets_adult += int(tickets[2])
    number_tickets_senior += int(tickets[3])
        
    total_tickets = total_tickets + int(tickets[0])
    total_tickets = total_tickets + int(tickets[1])
    total_tickets = total_tickets + int(tickets[2])
    total_tickets = total_tickets + int(tickets[3])
    
    total_price = (number_tickets_baby * tickets_prices['baby'] + number_tickets_kid * tickets_prices['kid']+\
                   number_tickets_adult * tickets_prices['adult'] + number_tickets_senior * tickets_prices['senior']) 
    
    line_transaction = tickets_file.readline()

print("Baby tickets..: {:3d} -   {:7.2f}$".format(number_tickets_baby, number_tickets_baby * tickets_prices['baby']))
print("Kid tickets...: {:3d} -   {:7.2f}$".format(number_tickets_kid, number_tickets_kid * tickets_prices['kid'])), 
print("Adult tickets.: {:3d} -   {:7.2f}$".format(number_tickets_adult, number_tickets_adult * tickets_prices['adult']))
print("Senior tickets: {:3d} -   {:7.2f}$".format(number_tickets_senior, number_tickets_senior * tickets_prices['senior']))

print("\nTotal: {:3d} - {:7.2f}$".format(total_tickets, total_price))
