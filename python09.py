#type conversion
first_number=input("enter the first number:")
second_number=input("enter the second number:")

result= first_number + second_number
print(result)
dt=type(first_number)
print(dt)
#<class 'str'>

print("we need to convert datatype")

print("""type conversion have 2 types:
1. implicit type conversion : by python interpreter automatically
2. explicit type conversion : by user manually""")

#implicit type conversion
num1=1
num2=1.1
print(num1+num2)#answer is 2.1

num3=5
num4=1+2j
print(num3+num4)#(6+2j)
print(type(num3+num4))#<class 'complex'>

#explicit type conversion
new_first_number=int(first_number)
print(type(new_first_number))

a=0b1010 
#a=10
print(type(a))
b=0x12c
#b=300
print(type(b)) 
print(a)
print(b)

true_or_false1=bool(1)
print(true_or_false1)
#true
true_or_false2=bool(-1)
print(true_or_false2)
#true

float_a=float(4)
print(float_a)

complexity=4j
print("complexity=",complexity)
print(complexity.real)
print(complexity.imag)

list1=list("hello")
print(list1)
