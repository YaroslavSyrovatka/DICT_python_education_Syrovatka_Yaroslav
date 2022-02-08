# print("Loan principal: 1000\nMonth 1: repaid 250\nMonth 2: repaid 250\nMonth 3: repaid 500\n"
#       "The loan has been repaid!")
import math

loan_principal = int(input("Enter the loan principal:\n>"))
a = input("""What do you want to calculate?
type "m" – for number of monthly payments,
type "p" – for the monthly payment:\n>""")
if a == "m":
    monthly_payment = int(input("Enter the monthly payment:\n>"))
    b = loan_principal / monthly_payment
    b = math.ceil(b)
    print(b)
if a == "p":
    number_of_months = int(input("Enter the number of months:\n>"))
    c = loan_principal / number_of_months
    c = math.ceil(c)
    d = loan_principal - (number_of_months - 1) * c
    if c == d:
        print("Your monthly payment = ", c)
    else:
        print("Your monthly payment = ", c, "and the last payment =", d)