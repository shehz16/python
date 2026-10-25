field1 = 450
field2 = 60
field3 = 100
field4 = 200
field5 = 90

total_field = field1 + field2 + field3 + field4 + field5
Average_field = total_field / 5
print("Total field: ", total_field)
print("Average field: ", Average_field)

per_kg_cost = 5
total_cost = total_field * per_kg_cost
print("Total earnings: ", total_cost)

bags = total_field // 50
remaining_field = total_field % 50
print("Total bags: ", bags)
print("Remaining field (kg):", remaining_field)

last_year_field = 400
print("better than last year: ", total_field > last_year_field)
print("worse than last year: ", total_field < last_year_field)
print("same as last year: ", total_field == last_year_field)

total_harvest += 50
print("updated total harvest after adding 50 kg: ", total_harvest)

total_harvest -= 30
print("updated total harvest after subtracting 30 kg: ", total_harvest)
bags total = total_harvest // 50
print("updated total bags after adding and subtracting: ", bags_total)