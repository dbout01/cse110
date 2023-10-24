print("Hello. Please verify your information.")

first = input('What is your first name? ')
last = input('What is your last name? ').upper()
job = input('What is your job title? ').capitalize()
id_num = input('Enter your ID number: ')
email = input('What is your email address? ').lower()
phone = input('What is your phone number? ')
hair = input("What is your hair color: ")
eye = input("What is your eye color: ")
birth_month = input("What is your birth month?: ")
train = input("Are you trained? [yes/no]: ")
 
output = f"""
The ID Card is:
---------------------------------------------------------
{last.upper()}, {first.capitalize()}
{job.title()}
ID: {id_num}
 
{email}
{phone}

Hair: {hair.capitalize():20} Eyes: {eye.capitalize()}
Month: {birth_month.capitalize():19} Training: {train.capitalize()} 
---------------------------------------------------------
"""
print(output)