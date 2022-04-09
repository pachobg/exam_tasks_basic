number_of_people = int(input())
night_over = int(input())
transport_maps = int(input())
museum_tickets = int(input())

night_over_price = night_over * 20
transport_maps_price = transport_maps * 1.60
museum_tickets_price = museum_tickets * 6

total_price_per_people = night_over_price + transport_maps_price + museum_tickets_price
price_for_all_people = total_price_per_people * number_of_people

tax = price_for_all_people * 0.25

final_price = price_for_all_people + tax

print(f"{final_price:.2f}")
