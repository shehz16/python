print("==============")
print("welcome to the ride.py program!")
print("==============")

print("step1: choose a ride type")
print("1. CAR")
print("2. BIKE")
print("3. MOTORCYCLE")
choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
    print("You have chosen a CAR ride")
    print("step2: choose a car type")
    print("1. SEDAN")
    print("2. SUV")
    print("3. TRUCK")
    car_choice = input("Enter your car choice (1, 2, or 3): ")
    if car_choice == "1":
        print("You have chosen a SEDAN.")
    elif car_choice == "2":
        print("You have chosen a SUV.")
    elif car_choice == "3":
        print("You have chosen a TRUCK.")
if choice == "2":
    print("You have chosen a BIKE ride.")
    print("step2: choose a bike type")
    print("1. MOUNTAIN")
    print("2. ROAD")
    print("3. ELECTRIC")
    bike_choice = input("Enter your bike choice (1, 2, or 3): ")
    if bike_choice == "1":
        print("You have chosen a MOUNTAIN bike.")
    elif bike_choice == "2":
        print("You have chosen a ROAD bike.")
    elif bike_choice == "3":
        print("You have chosen an ELECTRIC bike.")
if choice == "3":
    print("You have chosen a MOTORCYCLE ride.")
    print("step2: choose a motorcycle type")
    print("1. SPORT")
    print("2. TOURING")
    print("3. CUSTOM")
    motorcycle_choice = input("Enter your motorcycle choice (1, 2, or 3): ")
    if motorcycle_choice == "1":
        print("You have chosen a SPORT motorcycle.")
    elif motorcycle_choice == "2":
        print("You have chosen a TOURING motorcycle.")
    elif motorcycle_choice == "3":
        print("You have chosen a CUSTOM motorcycle.")