'''
Project: ZeroOut - Financial Calculator
By: Sam Kelly
Date: 6.16.25
'''

def calculate(debtValue, rate, numberOfPayPeriods):
    return (rate * debtValue * (1+rate)** numberOfPayPeriods)/((1+rate)**numberOfPayPeriods-1)

def main():
    print("Hi! Welcome to ZeroOut. You can use this calculate payoff stategies based on your current debt amount, and interest rate.")
    totalDebt_str = input("Please enter your total debt: ")
    APR_str = input("Please enter your APR: ")
    NPER_str = input("Please enter your desired number of pay periods (in months - ex. 5, 12, 36, etc.,): ")

    #convert string values to their number/float alternatives
    interestRate = float(APR_str) / 12
    totalDebt = float(totalDebt_str)
    payPeriods = int(NPER_str)

    payment = round(calculate(totalDebt, interestRate, payPeriods), 2)
    print(f"Based on the provided values, to pay off your debt in {NPER_str} months, you would need to pay ${payment} per month.")

main()
    
