# Park operating data:
general_ticket = 40.00
child_ticket = 30.00
child = 11
senior =  55
senior_rate = 0.88
student_rate = 0.90
military: False
military_rate: 0.80
early_entry = 18
early_rate = 0.15
week_day = True

# Get user input:
children_count = int(input(f'How many children are {child} years or younger?: '))
adult_count = int(input(f'How many people are older than {child} and younger than {senior}?: '))
senior_count = int(input(f'How many seniors {senior} and older do you have?: '))
military_check = input(f'Is anyone in your party a member of the armed services? [yes/no]: ')
student_check = int(input(f'How many students are in your group?: '))

#Setup logic:
if 'yes' in military_check.lower():
    military = True
current_hour = 17 # TODO: Actually check date and time
# TODO: Actually check what day of week it is

#Calculate the ticket cost:
child_cost = 0
adult_cost = 0
senior_cost = 0
if military:
    if current_hour < early_entry:
        child_cost = child_ticket * military_rate * early_rate * children_count
        adult_cost = general_ticket * military_rate * early_rate * adult_count
        senior_cost = general_ticket * military_rate * early_rate * senior_count
    else:
       child_cost = child_ticket * military_rate * children_count
       adult_cost = general_ticket * military_rate * adult_count
       senior_cost = general_ticket * military_rate * senior_count 
else:
    child_cost = child_cost * children_count
    senior_count = general_ticket * military_rate * senior_rate
    if student_check > 0:
        # Account for some students:
        adults_remaining = adult_count - student_check
        adult_cost = general_ticket * adults_remaining
        adult_cost += general_ticket * student_rate * student_check