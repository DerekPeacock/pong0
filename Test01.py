global number, isJumping
number = 5
isJumping = True

def someFunction():
    "This prints out the global variable isJumping"

    global number, isJumping
    print()

    if(isJumping == False):
        print("someFunction isJumping = ", isJumping)
    
    if(number == 7):
        print("someFunction number = ", number)

    number = 6
    isJumping = True

    return

print("Testing Python Functions")
print()

number = 7
isJumping = False

print()
print("Global isJumping = ", isJumping)
print("Global Number = ", number)

someFunction()

print()
print("Global isJumping = ", isJumping)
print("Global Number = ", number)
