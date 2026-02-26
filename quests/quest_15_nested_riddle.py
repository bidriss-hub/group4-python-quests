direction = input("Do you go left or right? ")

if direction == "left":
    action = input("Do you swim or wait? ")
    
    if action == "swim":
        print("You found the treasure!")
    else:
        print("You waited too long. The treasure is gone.")
else:
    print("You fell into a trap.")