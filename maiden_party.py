maiden_party_budget = float(input())
love_letters = int(input())
roses = int(input())
key_holders = int(input())
pictures = int(input())
surprise_luck = int(input())

letters_price = love_letters * 0.60
roses_price = roses * 7.20
key_holder_price = key_holders * 3.60
surprise_luck_price = surprise_luck * 22
pictures_price = pictures * 18.20
product_number = love_letters + roses + key_holders + pictures + surprise_luck
money = letters_price + roses_price + key_holder_price + surprise_luck_price + pictures_price

if product_number > 25:
    money = money - money * 0.35

tax = money * 0.10

profit = money - tax

if profit >= maiden_party_budget:
    difference = profit - maiden_party_budget
    print(f"Yes! {difference:.2f} lv left.")
else:
    difference = maiden_party_budget - profit
    print(f"Not enough money! {difference:.2f} lv needed.")
