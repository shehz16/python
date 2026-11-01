temperature = int(input("Enter the temperature in Celsius: "))
if temperature < 20:
    outfit = "jacket"
    print("It's cold outside. Wear a jacket!")
    print("You might want to stay indoors.")
else:
    outfit = "t-shirt"
    print("It's warm outside. Wear a t-shirt!")
    print("You can go outside and enjoy the weather.")
israining = input("Is it raining? (yes/no): ").strip().lower()
if israining == "yes":
    print("It's raining. Don't forget your umbrella!")
wind_speed = int(input("Enter the wind speed in km/h: "))
if wind_speed > 30:
    print("It's windy. Be careful while walking outside!")
has_puddles = input("Are there puddles on the ground? (yes/no): ").strip().lower()
if has_puddles == "yes":
    print("Watch out for puddles! Wear waterproof shoes.")
print("")
print("weather check completed. Stay safe and enjoy your day!")
print("=== Weather outfit picker ===")
print("Temperature: ", temperature, )
print("outfit chosen: ", outfit)
print("raining: ", israining)
print("wind speed: ", wind_speed)
print("puddles: ", has_puddles)
print("=== End of weather check ===")