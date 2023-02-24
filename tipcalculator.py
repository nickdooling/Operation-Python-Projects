print("Welcome to the tip calculator")

total_bill = float(input("What is the total bill?\n"))
percentage = int(input("What percent would you like to leave?\n"))
amount_of_friends = int(input("How many people will you be splitting this with?\n"))

percentage_calc = total_bill * float(percentage / 100)
total_plus_tip = total_bill + percentage_calc
amount_of_friends_calc = float(total_plus_tip / amount_of_friends)
new_total = round(amount_of_friends_calc, 2)

message = (f"The total each person will pay is {new_total}")

print(message)