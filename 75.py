musclePain = False
fever = True
weakness = True

print("suspiction of influenza" if musclePain and fever and weakness else "The flu is unlikely")

if musclePain and fever and weakness:
    print("suspiction of influenza")
elif not (fever and musclePain) and weakness:
    print("Just take a rest!")
else:
    print("you may be cold")

isMan = True

if (musclePain and fever and weakness) or (isMan and (musclePain or fever or weakness)):
    print("suspiction of influenza")
elif not (fever and musclePain) and weakness:
    print("Just take a rest!")
else:
    print("you may be cold")

isCheckCompleted = False
print("Everything has been checked" if isCheckCompleted else "You have not checked everything yet")
