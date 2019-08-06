from datetime import date


def daystoendofyear(year=date.today().year, month=date.today().month, day=date.today().day):
    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    return delta.days


print('Date: 2020-12-20 days to end of year: %d' % (daystoendofyear(2020, 12, 20)))

print('Date: 2020-11-29 days to end of year: %d' % (daystoendofyear(2020, 11, 29)))

print('Date: 2020-03-03 days to end of year: %d' % (daystoendofyear(2020, 3, 3)))

print('Date: TODAY days to end of year: %d' % (daystoendofyear()))


def printanimal(animal=''):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/
 '''
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`
    '''
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''

    if animal == 'cat':
        print(txt_cat)
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print("Correct values for the parameter are: cat, bear, bat")
        return False

    return True


if printanimal('cat'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')


if printanimal('dog'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')


if printanimal('bat'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')


if printanimal('33'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
