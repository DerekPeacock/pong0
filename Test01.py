isJumping = True   

print("Testing Python Functions")
print()
print("Before function, isJumping = ", isJumping)

def someFunction():
    "This changes the global variable isJumping"
    global isJumping
    isJumping = False

someFunction()

print("After function, isJumping = ", isJumping)
