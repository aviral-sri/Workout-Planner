import random
from gtts import gTTS
import time
'''this project is under construction,
you can generate a workout plan according to you prefrence...
but for now you cant save it or use it while working out...
'''


def plan_workout():

    def user_preffn():
        user_age = int(input("Your Age::"))
        user_height = int(input("Your Height(in cm)::"))
        user_weight = int(input("Your Weight(in kg)::"))
        user_gender = input("Your Gender(M/F)::")
        user_bmi = user_weight / (user_height / 100 * user_height / 100)
        user_pref = {
            "user_age": user_age,
            "user_height": user_height,
            "user_weight": user_weight,
            "user_gender": user_gender,
            "user_bmi": user_bmi
        }
        return user_pref

    def user_is_male_undewight():
        if user_pref["user_age"] >= 18:
            from MaleWorkouts import underweight_male_above18_exercises
            selected_exercises = random.sample(
                list(underweight_male_above18_exercises.keys()), 10)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        elif user_pref["user_age"] < 18:
            from MaleWorkouts import underweight_male_under_18_exercises
            selected_exercises = random.sample(
                list(underweight_male_under_18_exercises.keys()), 8)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        else:
            print("either there was error in code or your input is wrong")

    def user_is_male_normalweight():
        if user_pref["user_age"] >= 18:
            from MaleWorkouts import normal_weight_over_18_exercises
            selected_exercises = random.sample(
                list(normal_weight_over_18_exercises.keys()), 14)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        elif user_pref["user_age"] < 18:
            from MaleWorkouts import normal_weight_under_18_exercises
            selected_exercises = random.sample(
                list(normal_weight_under_18_exercises.keys()), 10)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        else:
            print("either there was error in code or your input is wrong")

    def user_is_male_overweight():
        if user_pref["user_age"] >= 18:
            from MaleWorkouts import overweight_over_18_exercises
            selected_exercises = random.sample(
                list(overweight_over_18_exercises.keys()), 13)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        elif user_pref["user_age"] < 18:
            from MaleWorkouts import overweight_under_18_exercises
            selected_exercises = random.sample(
                list(overweight_under_18_exercises.keys()), 10)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        else:
            print("either there was error in code or your input is wrong")

    def user_is_female_undewight():
        from FemaleWorkouts import underweight_female_exercises
        if user_pref["user_age"] >= 18:
            selected_exercises = random.sample(
                list(underweight_female_exercises.keys()), 10)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        elif user_pref["user_age"] < 18:
            selected_exercises = random.sample(
                list(underweight_female_exercises.keys()), 8)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        else:
            print("either there was error in code or your input is wrong")

    def user_is_female_normalweight():
        from FemaleWorkouts import normal_weight_female_exercises
        if user_pref["user_age"] >= 18:
            selected_exercises = random.sample(
                list(normal_weight_female_exercises.keys()), 14)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        elif user_pref["user_age"] < 18:
            selected_exercises = random.sample(
                list(normal_weight_female_exercises.keys()), 10)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        else:
            print("either there was error in code or your input is wrong")

    def user_is_female_overweight():
        from FemaleWorkouts import overweight_female_exercises
        if user_pref["user_age"] >= 18:
            selected_exercises = random.sample(
                list(overweight_female_exercises.keys()), 13)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        elif user_pref["user_age"] < 18:
            selected_exercises = random.sample(
                list(overweight_female_exercises.keys()), 10)
            print("Here is your workout Plan:")
            exercise_string = "\n".join(selected_exercises)
            print(exercise_string)
            return exercise_string

        else:
            print("either there was error in code or your input is wrong")

    user_pref = user_preffn()
    if user_pref["user_gender"] == "M":
        print(user_pref["user_bmi"])
        if user_pref["user_bmi"] < 18.5:
            print("--------------------")
            print("You are underweight")
            return user_is_male_undewight()
        elif 18.5 < user_pref["user_bmi"] < 24.9:
            print("--------------------")
            print("You are normal weight")
            return user_is_male_normalweight()
        elif user_pref["user_bmi"] > 24.9:
            print("--------------------")
            print("You are overweight")
            return user_is_male_overweight()
        else:
            print("error")

    if user_pref["user_gender"] == "F":
        if user_pref["user_bmi"] < 18.5:
            print("--------------------")
            print("You are underweight")
            return user_is_female_undewight()
        elif 18.5 < user_pref["user_bmi"] < 24.9:
            print("--------------------")
            print("You are normal weight")
            return user_is_female_normalweight()
        elif user_pref["user_bmi"] > 24.9:
            print("--------------------")
            print("You are overweight")
            return user_is_female_overweight()
        else:
            print("either there was error in code or your input is wrong")


#this runs after 2nd option
def start_workout():
    print("--------------------")
    with open("myworkout.txt", "r") as file:
        work_list = file.read()
        exercise_list = work_list.split("\n")

    def print_list_with_delay(lst):
        #this funtion is made with the help of chat gpt
        for item in lst:
            print(item)
            for i in range(30, 0, -1):
                print(i, end=' ', flush=True)
                time.sleep(1)  # Wait for 1 second for countdown
            print()  # Print a newline after countdown

        print("Done!")

    print_list_with_delay(exercise_list)


while True:
    print("\nWorkout Planner Menu:")
    print("1. Generate Workout Plan")
    print("2. Start Workout")
    print("3. Display Workout Schedule")
    print("4. Exit")

    user_input = int(input("Please select one option::"))
    if user_input == 1:
        print(
            "Please Give the following details correctly to generate your Workout Plan"
        )
        with open("myworkout.txt", "w") as file:
            file.write(str(plan_workout()))

    elif user_input == 2:
        print("starting your workout")
        start_workout()
    elif user_input == 3:
        print("option 3 under construction")
    elif user_input == 4:
        print("ok exit")
        break
    else:
        print("either there was error in code or your input is wrong")
