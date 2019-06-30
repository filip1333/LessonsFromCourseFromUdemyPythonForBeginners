Clubs={'Inter' : 'Italy', 'Barcelona' : 'Spain'}
print(Clubs)
print(Clubs['Inter'])
Clubs['Motor'] = 'Polska'
print(Clubs)
print(Clubs.values())
print(Clubs.items())
print(Clubs.keys())
print(Clubs.popitem())
print(Clubs.setdefault('OM', 'France'))
print(Clubs)
NewClubs = {'AIK' : 'Sweden', 'OB' : 'Denmark', 'Barcelona' : 'France'}
print(NewClubs)
Clubs.update(NewClubs)
print(Clubs)