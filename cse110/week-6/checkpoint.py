print("""Thanks for applying for a loan. Please provide the information below to see if you are eligible.
Please provide a 1-10 rating for each category""")
loan_size = int(input('How large is the loan?: '))
credit_his = int(input('How good is your credit history?: '))
income = int(input('How high is your income?: '))
downpymt = int(input('How large is your down payment?: '))

should_loan = False


if loan_size >= 5:
    if credit_his >=7 and income >= 7:
        should_loan = True
    elif credit_his >=7 or income >= 7: #elif- only one has to be true
        if downpymt >= 5:
            should_loan = True
        elif downpymt < 5:
            should_loan = False
    else:
        should_loan = False
elif loan_size < 5:
    if credit_his < 4:
        should_loan = False
    else:
        if income >= 7 or downpymt >= 7:
            should_loan = True
        elif income >=4 and downpymt >=4:
            should_loan = False

if should_loan:
    print("Yes.")
else:
    print("No.")