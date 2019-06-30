Tax = (4, 7, 8, 23)
print(Tax[2])
print(Tax)
print(Tax[-1])
print(Tax.count(8))
print(Tax.index(4))
print(max(Tax))
TaxList = list(Tax)
print(TaxList)
TaxList.append(30)
print(TaxList)
NewTax = tuple(TaxList)
print(NewTax)
(tax1, tax2, tax3, tax4) = Tax
print(tax1, tax2, tax3, tax4)
a=1
b=10
print("a =", a, "\tb =", b)
#temp = a
#a=b
#b=temp
(a,b)=(b,a)
print("a =", a, "\tb =", b)