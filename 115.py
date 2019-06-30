import math

degree = 360
radian = degree * math.pi / 180
print("%d degree is %f radians" % (degree, radian))
print('')

degree = 45
radian = degree * math.pi / 180
print('%d degree is %f radians' % (degree, radian))
print('')

print(math.radians(360))
print('')

print(math.radians(45))
print('')

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

small_area = math.pi * small_pizza_r**2
big_area = math.pi * big_pizza_r**2
family_area = math.pi * family_pizza_r**2
print("Small pizza area is", small_area)
print('Big pizza area is', big_area)
print('Family pizza area is', family_area)
print('')

print('Price for one small pizza square meter is', small_pizza_price/small_area)
print('Price for one big pizza square meter is', big_pizza_price/big_area)
print('Price for one family pizza square meter is', family_pizza_price/family_area)
print('')
