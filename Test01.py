global number
number = 5

def someFunction():
    "This prints out the global variable isJumping"
    print("Function Starts!")

    global number

    if(number == 7):
        print(number)

    if(isJumping):
        print("isJumping = ", isJumping)
    
    #isJumping = False
    print("Number = ", number)

    number = 6
    return

print("Testing Python Functions")
print()
global isJumping
isJumping = True
number = 7
someFunction()
print("Global isJumping = ", isJumping)
print("Number = ", number)
