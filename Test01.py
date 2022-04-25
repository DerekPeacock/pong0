def someFunction():
    "This prints out the global variable isJumping"

    print("Function Starts!")
    # isJumping = False
    if(isJumping):
        print("isJumping = ", isJumping)
    
    # isJumping = False

    return

print("Testing Python Functions")
print()
isJumping = True
someFunction()
print("Global isJumping = ", isJumping)
