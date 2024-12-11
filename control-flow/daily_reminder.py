task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time_bound.lower() == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a high priority task. Consider completing it as soon as possible."
    case "medium":
        if time_bound.lower() == "yes":
            reminder = f"'{task}' is a medium priority task that requires attention today!"
        else:
            reminder = f"Note: '{task}' is a medium priority task. Consider completing it when you have some time."
    case "low":
        if time_bound.lower() == "yes":
            reminder = f"'{task}' is a low priority task that requires attention today!"
        else:
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
print(reminder)
