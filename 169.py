import datetime
import os

data_input = r'/home/filip/PycharmProjects/Udemy/data_input'
data_output = r'/home/filip/PycharmProjects/Udemy/data_output'
today = datetime.date.today()
today_output = os.path.join(data_output, today.strftime("%Y-%m-%d"))
is_input_ok = os.path.isdir(data_input)
is_output_ok = os.path.isdir(data_output)
is_today_output_ok = not(os.path.isdir(today_output)) and not(os.path.isfile(today_output))

if is_input_ok and is_output_ok and is_today_output_ok:
    print('Conditions met! We can continue!')
else:
    print('Conditions not met! Check the paths!')

    if not is_input_ok:
        print("Input catalog %s must exist!" % data_input)
    if not is_output_ok:
        print("Output catalog %s must exist!" % data_output)
    if not is_today_output_ok:
        print("Today's output %s cannot exist (neither as file nor as directory)!" % today_output)
