print()
print("""Welcome to the Adventure Game. All choices are in CAPS.""")
ans = input("""You are walking through a dark forest and find three items: a MATCH, a FLASHLIGHT, and a LIGHTER. Which
one do you want to pick up?: """)


#IF STATEMENT - MATCH:
if ans == 'match'.lower():
    ans = input("""You pick up the match and strike it, and for an instant, the forest around you is illuminated.
        You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?: """)
    #RUN - option 1:
    if ans == 'run'.lower():
        ans = input("""You run and the grizzly bear catches up to you. You have no choice but to fight it or accept your death.
            Do you want to FIGHT, accept DEATH, or BREAKDANCE?: """)
        if ans == 'fight'.lower(): #if there are two choices in one sub-question, add an 'if' and 'else'
            print("""You fight it and a struggles ensues. You break the bears arm but it slashes your throat open
            and nearly decapitates you.""")
        elif ans == 'breakdance'.lower():
            print("""You decide to breakdance and the bear stars dancing with you. Soon an old lady riding on a strange creature
            joins you and the bear and you all go to her house for some cookies and wine.""")
        else:
            print("""You accept death, but then all of the sudden, a little old lady riding a strange creature appears
                out of nowhere, saves you, and takes you to their house for cookies and wine.""")
    #HIDE - option 2:
    if ans == 'hide'.lower():
        ans = input("""You hide behind a tree and all of the sudden, a little old lady appears and offers to take you in.
        Do you ACCEPT or REFUSE her invitation?: """)
        if ans == 'accept'.lower():
            print("""You accept her invitation and she lets you inside her house and gives you cookies and wine
            and offers you a place to stay for the night.""")
        else:
            print("""You refuse her invitation and she sends her pet monster, a strange creature, to eat you.
            You die by getting your intestines ripped out.""")


#ELIF STATEMENT - FLASHLIGHT:
elif ans == 'flashlight'.lower():
        ans = input("""You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also
        heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?: """)
        #FOLLOW - option 1:
        if ans == 'follow'.lower():
            ans = input("""You follow the path and you eventually come upon a house. You aren\'t sure if you want to go inside or not,
            because you dont want to risk anything. Do you want to go INSIDE the house or go AROUND it?: """)
            if ans == 'inside'.lower():
                print("""You go inside the house and you meet a little old lady. She gives you cookies and wine and sends you on your way.""")
            else:
                print("""You go around the house and your ambushed by a strange creature from the trees, and you die.""")
        #LOOK - option 2:
        if ans == 'look'.lower():
            ans = input("""You look in the trees and you see a strange creature lunge out at you. You\'re pretty scared at this point
            but do you decide to FIGHT it or RUN?: """)
            if ans == 'fight'.lower():
                print("""You fight the creature but lose when it pulls your head off your body.""")
            else:
                print("""You run from the creature but it catches up to you, gets ahold of your legs, and rips you in-half.""")      


#ELSE STATEMENT - LIGHTER:
elif ans == 'lighter'.lower():
    ans = input("""You pick up the lighter and strike it, and for an instant, the forest around you is illuminated. A little old lady appears
    out of nowhere and asks you if she can use the lighter for her cigarette. Do you ALLOW her to use it or REFUSE?: """)
    #ALLOW - option 1:
    if ans == 'allow'.lower():
        ans = input("""You allow her to use the lighter and she takes a long drag and blows the smoke in your face. She then invites you to her place
        with a kindly look on her face. ACCEPT or TURN AWAY her invitation?: """)
        if ans == 'accept'.lower():
            print("""You accept her invitation and she ends up being pretty chill and gives you cookies and wine.""")
        else:
            print("""She gets angry and stabs you in the throat and you die.""")
    #REFUSE - option 2:
    if ans == 'refuse'.lower():
        ans = input("""You refuse her request to let her use your lighter and she says she wants to kill you. Do you RUN or FIGHT her?: """)
        if ans == 'run'.lower():
            print("""You run and she sends a strange creature after you and it takes the cigarette that the old lady used and shoves it down
            your throat, burning you. You die.""")
        else:
            print("""You fight her and you win, but all of a sudden a strange creature comes out of the shadows and it snaps your neck.""")


    
    else:
        print("""Invalid entry""")

else:
    print("""Invalid entry""")





# STRUCTURE OF STATEMENTS #
#
# if statement - match:
#----------------------------------
# RUN - option 1
# if ans ==
#     ans =
#     if ans ==
#         print
#     elif ans ==
#           print
#     else:
#           print
#
# HIDE - option 2
#     if ans ==
#       ans =
#       if ans ==
#           print
#       else =
#           print
#
#
#
#
# elif statement - flashlight:
#----------------------------------
# 
# FOLLOW - option 1
# elif ans ==
#     ans =
#     if ans ==
#         ans =
#     if ans ==
#         else:
#
# ALLOW - option 2
#      if ans ==
#       ans =
#       if ans ==
#           print
#       else:
#
#
#
#
#
# elif statement - lighter:
#----------------------------------
# 
# ALLOW - option 1
# elif ans ==
#     ans =
#     if ans ==
#         ans =
#     if ans ==
#         else:
#
# REFUSE - option 2
#      if ans ==
#       ans =
#           if ans ==
#             print
#           else:
#
#     else:
# else: