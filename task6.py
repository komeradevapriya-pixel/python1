distance = float(input("Enter distance in km: "))
age = int(input("Enter passenger age: "))
travel_class = input("Enter class (Sleeper/AC): ").lower()

if travel_class == "sleeper":
    fare = distance * 1
elif travel_class == "ac":
    fare = distance * 2
else:
    fare = 0

if age < 5:
    fare = 0
elif age >= 60:
    fare = fare * 0.8

fare = fare + 20
print("Railway Fare =", fare)