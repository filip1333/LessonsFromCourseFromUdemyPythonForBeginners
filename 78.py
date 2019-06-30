firsrRow = 1
lastRow = 31
currentRow = firsrRow

while currentRow <= lastRow:
    print('Row number: ', currentRow)
    currentRow += 1

firstNumber = 1
lastNumber = 13

number = firstNumber

while number <= lastNumber:
    print(number, number*number, number*number*number)
    number += 1

start = 0
end = 16
x = start

while x <= end:
    print(x, 2**x)
    x += 1

start = 1
end = 100

while start <= end:
    print('x'*start)
    start += 1
