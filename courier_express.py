kilograms = float(input())
delivery = input()
kilometers = int(input())

price = 0

if kilograms < 1:
    price = kilometers * 0.03
    if delivery == "express":
        fee = (0.03 * 0.8) * kilograms * kilometers
        price += fee

elif 1 <= kilograms < 10:
    price = kilometers * 0.05
    if delivery == "express":
        fee = (0.05 * 0.4) * kilograms * kilometers
        price += fee

elif 10 <= kilograms < 40:
    price = kilometers * 0.10
    if delivery == "express":
        fee = (0.10 * 0.05) * kilograms * kilometers
        price += fee

elif 40 <= kilograms < 90:
    price = kilometers * 0.15
    if delivery == "express":
        fee = (0.15 * 0.02) * kilograms * kilometers
        price += fee

elif 90 <= kilograms <= 150:
    price = kilometers * 0.20
    if delivery == "express":
        fee = (0.20 * 0.01) * kilograms * kilometers
        price += fee

print(f"The delivery of your shipment with weight of {kilograms:.3f} kg. would cost {price:.2f} lv.")