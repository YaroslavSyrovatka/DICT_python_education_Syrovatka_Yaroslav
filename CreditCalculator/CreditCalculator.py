# print("Loan principal: 1000\nMonth 1: repaid 250\nMonth 2: repaid 250\nMonth 3: repaid 500\n"
#       "The loan has been repaid!")
# import math
#
# loan_principal = int(input("Enter the loan principal:\n>"))
# a = input("""What do you want to calculate?
# type "m" – for number of monthly payments,
# type "p" – for the monthly payment:\n>""")
# if a == "m":
#     monthly_payment = int(input("Enter the monthly payment:\n>"))
#     b = loan_principal / monthly_payment
#     b = math.ceil(b)
#     print(b)
# if a == "p":
#     number_of_months = int(input("Enter the number of months:\n>"))
#     c = loan_principal / number_of_months
#     c = math.ceil(c)
#     d = loan_principal - (number_of_months - 1) * c
#     if c == d:
#         print("Your monthly payment = ", c)
#     else:
#         print("Your monthly payment = ", c, "and the last payment =", d)
import math
a = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
>""")
if a == "n":
    loan_principal = int(input("Enter the loan principal:\n>"))
    monthly_payment = int(input("Enter the monthly payment:\n>"))
    loan_interest = int(input("Enter the loan interest:\n>"))
    i = loan_interest * 0.01 / 12
    number_of_monthly_payments = math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i)
    number_of_monthly_payments = math.ceil(number_of_monthly_payments)
    year = number_of_monthly_payments / 12
    month = (year - math.floor(year)) * 12
    if math.floor(month) != 0:
        print(f"It will take {math.floor(year)} years and {math.ceil(month)} months to repay this loan!\n")
    else:
        print(f"It will take {math.ceil(year)} years to repay this loan!\n")
elif a == "a":
    loan_principal = int(input("Enter the loan principal:\n>"))
    number_of_periods = int(input("Enter the number of periods:\n>"))
    loan_interest = int(input("Enter the loan interest:\n>"))
    i = loan_interest * 0.01 / 12
    sym = pow(1 + i, number_of_periods)
    annual_payment = loan_principal * ((i * sym) / (sym - 1))
    print(f"Your monthly payment = {math.ceil(annual_payment)}!")
elif a == "p":
    annuity_payment = float(input("Enter the annuity payment:\n>"))
    number_of_periods = int(input("Enter the number of periods:\n>"))
    loan_interest = float(input("Enter the loan interest:\n>"))
    i = loan_interest * 0.01 / 12
    sym = pow(1 + i, number_of_periods)
    principal_loan_amount = float(annuity_payment / ((i * sym) / (sym - 1)))
    principal_loan_amount = math.floor(principal_loan_amount)
    print(f"Your loan principal = {principal_loan_amount}!")