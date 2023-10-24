#use this weeks materials as reference

rider_1_age = input('What is the age of the first rider?: ')
rider_1_height = input('What is the height of the first rider (in inches)?: ')





two_riders = False
one_rider = True
can_ride = False


# make sure to ask the user for this data
rider_1_age = 18
rider_1_height = 62 #inches
rider_check = input('Is there another rider?')





if 'yes' in rider_check.lower():
    two_riders = True
    # TODO make sure to ask the user for this data:
    rider_2_age = 11
    rider_2_height = 55 #inches





#check how many riders we have
if two_riders:
    #we have two riders
    if rider_1_age < 18 and rider_2_age < 18 and (rider_1_age >= 12 and rider_2_age >= 12):
        #if there are two riders both between 12 & 17:
        if rider_1_height >= 52 and rider_2_height >= 52:
            can_ride = True
    if rider_1_age >= 18 and rider_2_age >= 18 (rider_1_age < 18 and rider_2_age < 18):
        can_ride = True
else:
    #we have one rider / if one rider is at-least 18 years old & 62 in:
    if rider_1_age >= 18 and rider_1_height >= 62:
        can_ride = True
    else:
        can_ride = False





#tell the rider operator if thesecpeople can ride
if can_ride:
    print('Welcome! You may ride')
else:
    print('Sorry, you can not ride')