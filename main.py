import critter


critterName = "Goeffrey"
petName = critter.Critter(critterName)
petName.sleep()
while True:
    action = input("What would you like Geoffrey to do?")
    if action == "feed":
        petName.feed()
    elif action == "sleep":
        petName.sleep()
    elif action == "play":
        petName.play()