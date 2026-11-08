speed1 = int(input("Enter the speed of the first cyclist in km/h: "))
speed2 = int(input("Enter the speed of the second cyclist in km/h: "))
speed3 = int(input("Enter the speed of the third cyclist in km/h: "))

avg_speed = (speed1 + speed2 + speed3) / 3
print(f"The average speed of the three cyclists is: {avg_speed} km/h")

if avg_speed > speed1 and avg_speed > speed2 and avg_speed > speed3:
    print("The average speed is greater than the speed of all three cyclists.")
elif avg_speed > speed1 and avg_speed > speed2:
    print("The average speed is greater than the speed of the first two cyclists.")
elif avg_speed > speed1 and avg_speed > speed3:
    print("The average speed is greater than the speed of the first and third cyclists.")
elif avg_speed > speed2 and avg_speed > speed3:
    print("The average speed is greater than the speed of the second and third cyclists.")
elif avg_speed > speed1:
    print("The average speed is greater than the speed of the first cyclist.")
elif avg_speed > speed2:
    print("The average speed is greater than the speed of the second cyclist.")
else:
    print("The average speed is greater than the speed of the third cyclist.")