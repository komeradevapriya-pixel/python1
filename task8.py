material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
machine = float(input("Enter machine cost: "))
selling = float(input("Enter total selling price: "))

cost = material + labour + machine
profit = selling - cost

print("Total Cost =", cost)
print("Profit =", profit)

if profit > 0:
    print("Production is Profitable")
elif profit == 0:
    print("No Profit No Loss")
else:
    print("Production is at Loss")