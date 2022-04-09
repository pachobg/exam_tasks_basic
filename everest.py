
days = 1
high = 5364
goal_reached = False
while True:
    command = input()
    if command == "END":
        break
    meters_claim = int(input())
    if command == "Yes":
        days += 1
        high += meters_claim
    if command == "No":
        high += meters_claim
    if days > 5:
        high -= meters_claim
        break
    if high >= 8848:
        goal_reached = True
        break

if goal_reached:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(high)

