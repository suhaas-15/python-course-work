print("Assign multiple values to multiple variables")
num1,num2,num3=10,20,30
print("number1 values num1")
print("number1 values", num1)
print("number2 values" ,num2)
print("number3 values" ,num3)
print("all variable refference are:", id(num1), id(num2), id(num3))

print("assign single values to multi variable")
num1=num2=num3=10
print("num1 values", num1)
print("num2 value" , num2)
print("num3 value" , num3)
print("all variable reff are:", id(num1), id(num2), id(num3))

print("swaping variables")
a,b = 10,20
a,b = b,a
print("a,b")
print("swaping reff are:", id(a), id(b))
