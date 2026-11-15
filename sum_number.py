num = int(input("Enter a whole number whose sum you want to calculate: "))
total_sum = 0 

for i in range(1, num + 1):
    total_sum += i

print(f"The total sum of numbers from 1 to {num} is: {total_sum}")
