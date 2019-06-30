IsWeekend = False
print('Is weekend =',IsWeekend)

Temperature = 5
print('Temperature =',Temperature)

ToDoList='Shopping'
print('ToDoList =',ToDoList)

IsHappy = not IsWeekend and Temperature < 20 and ToDoList != ''
print('IsHappy=',IsHappy)


isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = False

turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
print('turnLightsOn =',turnLightsOn)
print("Automatic mode:",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:",isDirectLight)
print("Is it rainy:",isRainy)
print("TURNS LIGHTS ON",turnLightsOn)