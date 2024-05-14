#life in weeks
#input: age
#Output: number of weeks
age=int(input("Enter your age"))
life = 90
weeks_in_year=52
to_live = life - age
weeks_remaining = to_live*weeks_in_year
print(f"You have {weeks_remaining} weeks to live")