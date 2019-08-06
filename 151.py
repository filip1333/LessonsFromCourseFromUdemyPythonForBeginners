from datetime import date


def daystoendofyear(year=date.today().year, month=date.today().month, day=date.today().day):

    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print('Counting from', date_today, 'days remaining to end of year:', delta.days)


daystoendofyear(2020, 12, 20)
daystoendofyear(2021, 12, 21)
daystoendofyear(year=2022, month=12, day=22)
daystoendofyear(day=23, month=12, year=2023)
daystoendofyear()
daystoendofyear(month=9)
daystoendofyear(day=15)


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

    return


printanimal('cat')
