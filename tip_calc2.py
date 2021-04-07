# Total bill amount? 100
# Level of service? good
# Split how many ways? 5
# Tip amount: $20.00
# Total amount: $120.00
# Amount per person: $24.00


Bill = float(input("the total bill amount?"))

service = input("The level of service?")
if service.lower() == "good":
    tip = .2

elif service.lower() == "fair":
    tip = .15

elif service.lower() == "poor":
    tip = .10

number_of_people = int(input("How many people are splitting the bill?: "))

print("\n")

payment_per_person = ("%.2f" % round(float(((tip / 100 +1) * Bill) / number_of_people), 2))

result = Bill * tip

total = result + Bill

print("Tip amount: $ %.2f" % result)
print("total: $ %.2f" % total)

print(f"Each person owes: ${payment_per_person}")