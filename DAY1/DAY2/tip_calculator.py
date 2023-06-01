#If the bill was $150.00, split between 5 people, with 12% tip. 
print("welcome to the tip calculator")
bill = input("what was your total bill? $")
bill_fl = float(bill)
tip = int(input("how much percentage would you like to give? 10, 12 15"))
people = int(input("how many people to split the bill? "))
percentage_tip = tip/100 * bill_fl + bill_fl
print(percentage_tip)
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇