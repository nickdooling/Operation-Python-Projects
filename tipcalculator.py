print("Welcome to the tip calculator")

#this is where you are being asked what your initial bill is.
initial_bill = float(input("What is the initial bill?\n"))
#this is where you input the tip percentage.
percentage = int(input("What percent would you like to leave?\n"))
#this is where you will input how many people will be splitting the bill.
amount_of_friends = int(input("How many people will you be splitting this with?\n"))

#here you are calculating the tip
percentage_calc = initial_bill * float(percentage / 100)
#here you are adding the tip to the total
total_plus_tip = initial_bill + percentage_calc
#here you are dividing the total amongst the amount of people paying
amount_of_friends_calc = float(total_plus_tip / amount_of_friends)
#here you will be rounding the total to the nearest hundredth 
new_total = round(amount_of_friends_calc, 2)
#here you will be calculating how much each friend will be putting towards the tip
total_tip_per_person = percentage_calc / amount_of_friends

#the final message is compiled below 
message = (f"The total each person will pay is ${new_total}, with a tip total of ${percentage_calc}. Each person will pay a total of ${total_tip_per_person} for the tip.")

#finally, you print the message.
print(message)