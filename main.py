import random
import time
from datetime import datetime


def plan_workout():
    def user_preffn():
        try:
            user_age = int(input("Your Age: "))
            user_height = int(input("Your Height (in cm): "))
            user_weight = int(input("Your Weight (in kg): "))
            user_gender = input("Your Gender (M/F): ").upper()
            user_bmi = user_weight / ((user_height / 100) ** 2)
            user_pref = {
                "user_age": user_age,
                "user_height": user_height,
                "user_weight": user_weight,
                "user_gender": user_gender,
                "user_bmi": user_bmi
            }
            return user_pref
        except ValueError:
            print("Please enter valid inputs.")
            return None

    def generate_exercise_plan(workout_dict, num_exercises):
        selected_exercises = random.sample(list(workout_dict.keys()), num_exercises)
        print("Here is your workout Plan:")
        exercise_string = "\n".join(selected_exercises)
        print(exercise_string)
        return exercise_string

    user_pref = user_preffn()
    if not user_pref:
        return None

    print(f"Your BMI is: {user_pref['user_bmi']:.2f}")

    if user_pref["user_gender"] == "M":
        if user_pref["user_bmi"] < 18.5:
            print("You are underweight")
            if user_pref["user_age"] >= 18:
                from MaleWorkouts import underweight_male_above18_exercises as exercises
            else:
                from MaleWorkouts import underweight_male_under_18_exercises as exercises
        elif 18.5 <= user_pref["user_bmi"] < 24.9:
            print("You are normal weight")
            if user_pref["user_age"] >= 18:
                from MaleWorkouts import normal_weight_over_18_exercises as exercises
            else:
                from MaleWorkouts import normal_weight_under_18_exercises as exercises
        else:
            print("You are overweight")
            if user_pref["user_age"] >= 18:
                from MaleWorkouts import overweight_over_18_exercises as exercises
            else:
                from MaleWorkouts import overweight_under_18_exercises as exercises
    elif user_pref["user_gender"] == "F":
        if user_pref["user_bmi"] < 18.5:
            print("You are underweight")
            from FemaleWorkouts import underweight_female_exercises as exercises
        elif 18.5 <= user_pref["user_bmi"] < 24.9:
            print("You are normal weight")
            from FemaleWorkouts import normal_weight_female_exercises as exercises
        else:
            print("You are overweight")
            from FemaleWorkouts import overweight_female_exercises as exercises
    else:
        print("Invalid gender input.")
        return None

    num_exercises = 10 if user_pref["user_age"] >= 18 else 8
    return generate_exercise_plan(exercises, num_exercises)

def start_workout():
    print("--------------------")
    try:
        with open("myworkout.txt", "r") as file:
            work_list = file.read()
            exercise_list = work_list.split("\n")

        def print_list_with_delay(lst):
            for item in lst:
                print(item)
                for i in range(2, 0, -1):
                    print(i, end=' ', flush=True)
                    time.sleep(1)
                print()

            print("Done!")

        print_list_with_delay(exercise_list)
    except FileNotFoundError:
        print("Workout plan not found. Please generate a workout plan first.")

timelog = []
with open("streak.txt", "r") as file:
    streak = file.read()
streak = int(streak)

while True:
    print("Workout Planner Menu:")
    print("1. Generate Workout Plan")
    print("2. Start Workout")
    print("3. View Log")
    print("4. Exit")

    timestamp = str(datetime.now().date())

    try:
        user_input = int(input("Please select one option: "))
    except ValueError:
        print("Invalid input. Please select a valid option.")
        continue

    if user_input == 1:
        print("Please provide the following details correctly to generate your Workout Plan")
        workout_plan = plan_workout()
        if workout_plan:
            with open("myworkout.txt", "w") as file:
                file.write(workout_plan)
            timelog.append(timestamp)
            print("Workout plan generated and saved.")
        else:
            print("Failed to generate workout plan.")
        print("--------------------")

    elif user_input == 2:
        if streak == 0:
            print("Starting your workout")
            start_workout()
            timelog.append(timestamp)
        
        elif timestamp not in timelog:
            print("You have not logged any workout yet.")
            
            streak = str(streak + 1)
            with open("streak.txt", "w") as file:
                file.write(streak)
        elif timestamp in timelog:
            print("You have already done your workout today.")

    elif user_input == 3:
        print("Option 3 under construction")

    elif user_input == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option.")
