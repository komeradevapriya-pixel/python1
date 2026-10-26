venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
food = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))

sponsorship = float(input("Enter sponsorship amount: "))
contribution = float(input("Enter fee per participant: "))

total_cost = venue + equipment + food + transport + certificates
remaining = total_cost - sponsorship

print("Total Event Cost =", total_cost)
print("Sponsorship =", sponsorship)

if remaining <= 0:
    print("Event cost fully covered by sponsorship")
elif contribution > 0:
    participants = int(remaining / contribution)

    if remaining % contribution != 0:
        participants = participants + 1

    print("Minimum Participants Needed =", participants)
else:
    print("Participant contribution must be positive")