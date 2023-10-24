#---SCOPE---#

# x = 200
#stored in memory, but must be called (uncommented)


def myFunc():
    global x #not usually a good idea to declare a global inside a function
    x = 300 #local variable- only accessible inside the function
    # print(x)

myFunc()
print(x)