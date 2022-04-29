global isJumping
isJumping = False

def jumping():
    global isJumping 
    isJumping = True

def notJumping():
    global isJumping 
    isJumping= False

print("Testing Python Functions")
print()

jumping()
print("After Jumping(), isJumping = ", isJumping)

notJumping()
print("After notJumping(), isJumping = ", isJumping)
