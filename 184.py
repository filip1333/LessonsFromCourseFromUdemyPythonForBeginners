line = input('Enter some number: ')
filepath = input('Enter filename: ')
file = open(filepath, 'w+')
file.write(line)
file.close()


line = input('Enter some number: ')
filepath = input('Enter filename: ')
try:
    file = open(filepath, 'w+')
    file.write(line)
except:
    print('Sorry, we have an error')
file.close()


line = input('Enter some number: ')
filepath = input('Enter filename: ')
try:
    file = open(filepath, 'w+')
    file.write(line)
except FileNotFoundError:
    print('Sorry, we have an error, file not found')
except:
    print('Sorry, we have an error')
file.close()


line = input('Enter some number: ')
filepath = input('Enter filename: ')
try:
    file = open(filepath, 'w+')
    file.write(line)
    value = int(line)
    print("The value saved in file is ", value)
except FileNotFoundError:
    print('Sorry, we have an error, file not found')
except:
    print('Sorry, we have an error')
file.close()


line = input('Enter some number: ')
filepath = input('Enter filename: ')
try:
    file = open(filepath, 'w+')
    file.write(line)
    value = int(line)
    print("The value saved in file is ", value)
except FileNotFoundError:
    print('Sorry, we have an error, file not found')
except ValueError:
    print('Sorry, this value entered cannot be converted to a number')
except:
    print('Sorry, we have an error')
else:
    print('Actions completed successfully')
file.close()
