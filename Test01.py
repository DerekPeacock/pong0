global isJumping
isJumping = False

def Jumping():
    global isJumping 
    isJumping = True

def notJumping():
    global isJumping 
    isJumping = False

print("Testing Python Functions")
print()

Jumping()
print("After Jumping(), isJumping = ", isJumping)

notJumping()
print("After notJumping(), isJumping = ", isJumping)
