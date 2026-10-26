usage = float(input("Enter data usage in GB: "))
budget = float(input("Enter budget: "))

plan1 = 199
plan2 = 299
plan3 = 399

if usage <= 2 and plan1 <= budget:
    print("Best Plan: Plan 1")
elif usage <= 5 and plan2 <= budget:
    print("Best Plan: Plan 2")
elif usage <= 10 and plan3 <= budget:
    print("Best Plan: Plan 3")
else:
    print("No suitable plan available")