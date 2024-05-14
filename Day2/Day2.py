## Practice 1 - Digit Sum

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
str_num = str(two_digit_number)
sum = int(str_num[0]) + int(str_num[1])
print(sum)

##

## Practice 2 - BMI Calculator

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = int(float(weight)/(float(height)**2))
print(bmi)

##

## Practice 3 - Life in weeks

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

left_weeks = (90 - int(age))*52
print(f"You have {left_weeks} weeks left.")

##

## Day 2 Project: Tip Calculator

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = input("How much tip would you like to give? 10, 12, or 15? ")
people = int(input("How many people to split the bill? "))

split = total_bill * float("1." + tip_percent)/people

print(f"Each person should pay: ${round(split,2):.2f}")