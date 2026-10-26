budget = float(input("Enter budget in INR: "))
rate = float(input("Enter exchange rate (INR per foreign unit): "))
expense = float(input("Enter foreign currency expenses: "))
fee = float(input("Enter conversion fee in INR: "))

total = expense * rate + fee

print("Total Travel Cost in INR =", total)

if total <= budget:
    print("Within Budget")
else:
    print("Budget Exceeded")