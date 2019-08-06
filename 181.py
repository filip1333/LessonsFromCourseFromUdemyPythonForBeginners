import sys

file_path = r'c:\temp\data_input\orders.csv'


with open(file_path,"r") as file:

    for line in file:

        line = line.replace('\n','')
        order = line.split(',')

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                  (pharmacy_name, item, amount))
        except ValueError:
            print("Problem with conversion, check whether the amount is correct. Line: %s" % line)

        except IndexError:
            print("Missing information, check whether the line is build of at least 3 fields separated by comma. "
                  "Line: %s" % line)

        except:
            print("Oder error: %s" % sys.exc_info()[0])

print("Processing finished")
