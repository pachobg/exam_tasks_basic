days = int(input())
all_litters = 0
all_degrees = 0
for day in range(1, days + 1):
    litters = float(input())
    degrees = float(input())
    all_litters += litters
    degrees_per_litter = litters * degrees
    all_degrees += degrees_per_litter

average_degrees = all_degrees / all_litters

print(f"Liter: {all_litters:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
elif average_degrees > 42:
    print("Dilution with distilled water!")
