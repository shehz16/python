tempture = int(input("Enter the temperature in Celsius: "))
if tempture < 20:
    oufit = jacket
    print("It's cold outside. Wear a jacket!")
    print("You might want to stay indoors.")
else:
is it raining = input("Is it raining? (yes/no): ").strip().lower()
 if is it raining == "yes":
 print("It's raining. Don't forget your umbrella!")
 wind_speed = int(input("Enter the wind speed in km/h: "))
if wind_speed > 30:
 print("It's windy. Be careful while walking outside!")
 has puddles = input("Are there puddles on the ground? (yes/no): ").strip().lower()
 if has puddles == "yes":
print("Watch out for puddles! Wear waterproof shoes.")
print("")
print("weather check completed. Stay safe and enjoy your day!")
print("=== Weather outfit picker ===")
print("Temperature: ", tempture, )
print("outfit chosen: ", outfit)
print("raining: ", is it raining)
print("wind speed: ", wind_speed)
print("puddles: ", has puddles)
print("=== End of weather check ===")