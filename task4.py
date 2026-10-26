basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentive = float(input("Enter incentives: "))

gross = basic + allowance + overtime + incentive
deduction = gross * 0.10
net_salary = gross - deduction

print("Gross Salary =", gross)
print("Deduction =", deduction)
print("Net Salary =", net_salary)