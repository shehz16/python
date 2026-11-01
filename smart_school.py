print("=== smart school weather check ===")
print("Answer 3 questions to get your personalized plan for the day!")

day = input("What day is it today? (e.g., Monday, Tuesday, etc.): ")
weather = input("What is the weather like today? (e.g., sunny, rainy, cloudy): ")
homework_done = input("Have you completed your homework? (yes/no): ").strip().lower()

print()
print(f" your plan for {day} ===")
print("-" * 35)

if day in ["Saturday", "Sunday"]:
    print("It's the weekend! Enjoy your free time and relax.")
elif day == "Monday":
    print("It's Monday! Time to start the week with energy and focus on your studies.")
elif day == "Friday":
    print("It's Friday! Finish your tasks and get ready for the weekend.")
elif day in ["Tuesday", "Wednesday", "Thursday"]:
    print(f"It's {day}! Keep up the good work and stay productive.")
else:
    print("Invalid day input. Please enter a valid day of the week")

if weather == "sunny" and homework_done == "yes":
    print("The weather is sunny and you've completed your homework! Enjoy your day outside.")
elif weather == "sunny" and homework_done == "no":
    print("The weather is sunny, but you haven't completed your homework yet. Focus on your studies first!")
elif weather == "rainy" or weather == "cloudy":
    print("The weather is not ideal for outdoor activities. Stay indoors and complete your homework.")