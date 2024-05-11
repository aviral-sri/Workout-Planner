import random


def plan_workout():
  def user_preffn():
    user_age = int(input("Your Age::"))
    user_height = int(input("Your Height(in cm)::"))
    user_weight = int(input("Your Weight(in kg)::"))
    user_gender = input("Your Gender(M/F)::")
    user_bmi = user_weight / (user_height/100 * user_height/100)
    user_pref = {
      "user_age" : user_age,
      "user_height" : user_height,
      "user_weight" : user_weight,
      "user_gender" : user_gender,
      "user_bmi" : user_bmi

    }
    return user_pref



  def user_is_male_undewight():
    if user_pref["user_age"] >= 18:
      from MaleWorkouts import underweight_male_above18_exercises
      selected_exercises = random.sample(
        list(underweight_male_above18_exercises.keys()), 10)
      print("Here is your workout Plan:")
      for exercise in selected_exercises:
        print(exercise)

      return selected_exercises
    elif user_pref["user_age"] < 18:
      from MaleWorkouts import underweight_male_under_18_exercises
      selected_exercises = random.sample(
        list(underweight_male_under_18_exercises.keys()), 8)
     
      print("Here is your workout Plan:")
      for exercise in selected_exercises:
        print(exercise)

      return selected_exercises

    else:  
     print("either there was error in code or your input is wrong")

  def user_is_male_normalweight():
    if user_pref["user_age"] >= 18:
      from MaleWorkouts import normal_weight_over_18_exercises
      selected_exercises = random.sample(
        list(normal_weight_over_18_exercises.keys()), 14)
      print("Here is your workout Plan:")
      for exercise in selected_exercises:
        print(exercise)

      return selected_exercises
    elif user_pref["user_age"] < 18:
      from MaleWorkouts import normal_weight_under_18_exercises
      selected_exercises = random.sample(
        list(normal_weight_under_18_exercises.keys()), 10)

      print("Here is your workout Plan:")
      for exercise in selected_exercises:
        print(exercise)

      return selected_exercises
    else:  
     print("either there was error in code or your input is wrong")
      

  def user_is_male_overweight():
    if user_pref["user_age"] >= 18:
      from MaleWorkouts import overweight_over_18_exercises
      selected_exercises = random.sample(
        list(overweight_over_18_exercises.keys()), 13)
      print("Here is your workout Plan:")
      for exercise in selected_exercises:
        print(exercise)

      return selected_exercises
    elif user_pref["user_age"] < 18:
      from MaleWorkouts import overweight_under_18_exercises
      selected_exercises = random.sample(
        list(overweight_under_18_exercises.keys()), 10)

      print("Here is your workout Plan:")
      for exercise in selected_exercises:
        print(exercise)

      return selected_exercises
    else:  
     print("either there was error in code or your input is wrong")
    
  def user_is_female_undewight():
    from FemaleWorkouts import underweight_female_exercises
    if user_pref["user_age"] >= 18:
         selected_exercises = random.sample(
           list(underweight_female_exercises.keys()), 10)
         print("Here is your workout Plan:")
         for exercise in selected_exercises:
           print(exercise)

         return selected_exercises
    elif user_pref["user_age"] < 18:
         selected_exercises = random.sample(
           list(underweight_female_exercises.keys()), 8)

         print("Here is your workout Plan:")
         for exercise in selected_exercises:
           print(exercise)

         return selected_exercises
    else:  
      print("either there was error in code or your input is wrong")

  def user_is_female_normalweight():
    from FemaleWorkouts import normal_weight_female_exercises
    if user_pref["user_age"] >= 18:
         selected_exercises = random.sample(
           list(normal_weight_female_exercises.keys()), 14)
         print("Here is your workout Plan:")
         for exercise in selected_exercises:
           print(exercise)

         return selected_exercises
    elif user_pref["user_age"] < 18:
         selected_exercises = random.sample(
           list(normal_weight_female_exercises.keys()), 10)

         print("Here is your workout Plan:")
         for exercise in selected_exercises:
           print(exercise)

         return selected_exercises
    else:  
      print("either there was error in code or your input is wrong")

  def user_is_female_overweight():
    from FemaleWorkouts import overweight_female_exercises
    if user_pref["user_age"] >= 18:
         selected_exercises = random.sample(
           list(overweight_female_exercises.keys()), 13)
         print("Here is your workout Plan:")
         for exercise in selected_exercises:
           print(exercise)

         return selected_exercises
    elif user_pref["user_age"] < 18:
         selected_exercises = random.sample(
           list(overweight_female_exercises.keys()), 10)

         print("Here is your workout Plan:")
         for exercise in selected_exercises:
           print(exercise)

         return selected_exercises
    else:  
      print("either there was error in code or your input is wrong")
         
  
  user_pref = user_preffn()
  if user_pref["user_gender"] == "M":
    print(user_pref["user_bmi"])
    if user_pref["user_bmi"] < 18.5:
      print("--------------------")
      print("You are underweight")
      user_is_male_undewight()
    elif user_pref["user_bmi"] > 18.5 and user_pref["user_bmi"] < 24.9:
      print("--------------------")
      print("You are normal weight")
      user_is_male_normalweight()
    elif user_pref["user_bmi"] > 24.9:
      print("--------------------")
      print("You are overweight")
      user_is_male_overweight()
    else:
      print("error")

  if user_pref["user_gender"] == "F":
    if user_pref["user_bmi"] < 18.5:
      print("--------------------")
      print("You are underweight")
      user_is_female_undewight()
    elif user_pref["user_bmi"] > 18.5 and user_pref["user_bmi"] < 24.9:
      print("--------------------")
      print("You are normal weight")
      user_is_female_normalweight()
    elif user_pref["user_bmi"] > 24.9:
      print("--------------------")
      print("You are overweight")
      user_is_female_overweight()
    else:
      print("either there was error in code or your input is wrong")
  else:
    print("error")
    print("either there was error in code or your input is wrong")
  


while True:
  print("\nWorkout Planner Menu:")
  print("1. Generate Workout Plan")
  print("2. Log Completed Workout")
  print("3. Display Workout Schedule")
  print("4. Exit")

  user_input= int(input("Please select one option::"))
  if user_input == 1:
    print("Please Give the following details correctly to generate your Workout Plan")
    plan_workout()



  
  elif user_input == 2:
    print("option 2 under construction")
  elif user_input == 3:
   print("option 3 under construction")
  elif user_input ==  4:
    print("ok exit")
    break
  else:
    print("either there was error in code or your input is wrong")
    
      
    
    