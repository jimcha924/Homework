# Tip Calculator
# good = 20%
# fair = 15%
# poor = 10%

Bill = float(input("the total bill amount?"))

service = input("The level of service?")
if service.lower() == "good":
    tip = .2

elif service.lower() == "fair":
    tip = .15

elif service.lower() == "poor":
    tip = .10

result = Bill * tip

total = result + Bill

print("Tip amount: $ %.2f" % result)
print("total: $ %.2f" % total)


