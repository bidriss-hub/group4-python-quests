def forest():
    print("You are in a dark forest. You find a treasure! The End.")

def castle():
    print("You enter a spooky castle. You are trapped! The End.")

choice = input("Do you go to the forest or the castle? ")

if choice == "forest":
    forest()
else:
    castle()