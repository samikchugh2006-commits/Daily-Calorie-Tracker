# --------------------------------------------------------
# Name: Samik Chugh
# Course: Programming for Problem Solving using Python
# Title: Daily Calorie Tracker
# --------------------------------------------------------

print("Welcome to the Daily Calorie Tracker!")
print("This program helps you keep track of your meals and calories.\n")

# Step 1: Ask user how many meals they had
num_meals = int(input("How many meals did you eat today? "))

meals = []        # list to store meal names
calories = []     # list to store calories for each meal

# Step 2: Take meal name and calories input
for i in range(num_meals):
    name = input(f"\nEnter name of meal {i+1}: ")
    cal = float(input(f"Enter calories for {name}: "))
    meals.append(name)
    calories.append(cal)

# Step 3: Calculate total and average calories
total_calories = sum(calories)
average_calories = total_calories / num_meals

# Step 4: Ask user for daily limit
limit = float(input("\nEnter your daily calorie limit (e.g., 2000): "))

# Step 5: Compare total with limit
if total_calories > limit:
    status = "⚠️ You have exceeded your daily calorie limit!"
else:
    status = "✅ You are within your daily calorie limit."

# Step 6: Display all details neatly
print("\n----------------------------------------------------")
print("           DAILY CALORIE SUMMARY")
print("----------------------------------------------------")
print("Meal Name\t\tCalories")
print("----------------------------------------------------")
for i in range(num_meals):
    print(f"{meals[i]:<15}\t{calories[i]:>7.2f}")
print("----------------------------------------------------")
print(f"Total Calories:\t\t{total_calories:.2f}")
print(f"Average Calories:\t{average_calories:.2f}")
print("----------------------------------------------------")
print(status)
print("----------------------------------------------------")

