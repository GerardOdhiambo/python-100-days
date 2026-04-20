# Tip Calculator
print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
number_of_people = int(input("How many people to split the bill?"))

new_total_bill = total_bill + tip / 100 * total_bill
each_person_pay = new_total_bill / number_of_people
print(f"Each person should pay: \n${round(each_person_pay, 1)}")
