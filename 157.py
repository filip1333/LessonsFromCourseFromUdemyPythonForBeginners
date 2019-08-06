from datetime import date


def daystoendofyear(*dates):
    for date_today in dates:
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Counting from', date_today, 'days remaining to end of year:', delta.days)


daystoendofyear(date(2020, 12, 20))
daystoendofyear(date(2021, 12, 21), date(1000, 1, 5))
daystoendofyear(date(1950, 11, 5), date.today(), date(2000, 6, 28))


def printanimal(*animals):
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

    for animal in animals:
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
printanimal('bat')
printanimal('', 'cat', 'bat')
printanimal('bear', 'bat')
printanimal('1', '2', '3')
printanimal('xyz', 'cat')

