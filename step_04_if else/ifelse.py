# Example 1: Checking if the person is an adult or a teenager
age = 12

if age >= 18:
    print("You are an adult.")
else:
    print("You are a teenager.")

#----------------------------------------------------------

# Example 2: Checking the day of the week and providing appropriate messages
day_of_week = "Monday"

if day_of_week.lower() == "saturday" or day_of_week.lower() == "sunday":
    print("Enjoy the weekend!")
elif day_of_week.lower() == "monday":
    print("Go to school!")
elif day_of_week.lower() == "friday":
    print("It's Friday! Almost the weekend!")
else:
    print("It's a weekday, keep working hard.")

#----------------------------------------------------------

# Example 3: Checking if a number is positive, negative, or zero
number = -4

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#----------------------------------------------------------

# Example 4: Checking if a number is even or odd
digit = 3

if digit % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#----------------------------------------------------------

# Example 5: Checking if a person is eligible to vote based on age and citizenship
age = 20
citizenship = "Pakistan"

if age >= 18 and citizenship.lower() == "pakistan":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")