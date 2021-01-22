from calculate import calculate

days = int(input("How many days did you work : "))

basic_payment = 0
bonus_payment = 0
full_payment = 0

basic_payment = days*200
bonus_payment = calculate(days)
full_payment = basic_payment + bonus_payment

print("Daily payment - ", basic_payment)
print("+")
print("Bonus payment - ", bonus_payment)
print("---------------------------")
print("Full payment - ", full_payment)
