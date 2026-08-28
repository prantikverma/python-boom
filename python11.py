#OPERATORS IN PYTHON 
print("OPERATORS : used to perform operations on variables and values")
print("\n")
print("""OPERATORS ARE AS FOLLOWS:
1.ARITHMETIC OPERATORS
2.COMPARISON OPERATORS
3.LOGICAL OPERATORS
4.BITWISE OPERATORS
5.ASSIGNMENT OPERATORS
6.IDENTITY OPERATOR
7.MEMBERSHIP OPERATORS\n""")

#ARITHMETIC OPERATORS
print("""arithmetic operators contains:
a.addition
b.subtraction
c.multiplication
d.division
e.modulo\n""")

number1=11
number2=20

#addition operator
sum=number1+number2
print("sum=",sum)

#subtraction operator
dif=number1-number2
print("dif=",dif)

#multiplicsation operator
multi=number1*number2
print("product=",multi)

# true division operator
div=number1/number2
print("div=",div)

#modulus operator
remainder=number1%number2
print('remainder=',remainder)

#power operator
power=number1**number2
print(power)

#integer division:: quotient-->integer into float or float into integer
print(5//2)
#here 2.5 is converted into integer 2

print("lets go for the comparison operators\n")
#comparison operastors provide output as boolean
print("also called relational operators")
print(2>3)
print(2<3)
print(2==2)
print(2<=3)
print(2>=3)
print(2!=3)

#logical operators
x=True
y=False
z=True

print("""3 logical operators:
1.AND 
2.OR
3.NOT""")

#and logical operator
print(x and y)
print(x and z)

#or logical operator
print(x or y)

#not logical operator
print(not x)

print("\nbitwise operators\n")
print("bitwise operators work on binary numbers")
#used in image processing and robotics

bin1=2
bin2=3

#bitwise and  : &
print(bin1 & bin2)
#x=2=010
#y=3=011
#x&y=010=2

#bitwise or : |
print(bin1 | bin2)
#x=2=010
#y=3=011
#x|y=011=3

#
print(x>>2)

#
print(x<<3)

#ones complement
print(~bin1)

print("Assignment operators for now")
#ASSIGNMENT OPERATORS

num_a=1
print(num_a)
num_a+=3
#num_a=num_a+3
print(num_a)
num_a-=2
print(num_a)
num_a*=4
print(num_a)
num_a/=1
print(num_a)

a=4
b=2
print(a/b)
#true division outputs float

print("""in python there are no increment operator 
no a++
and no a--
only a=a+1
or a+=1""")

#IDENTITY OPERATORS
print("identity operator checks whether they belong to same memory location")

a=4
b=4
print(a is b)
#true

c="hello"
d='hello'
print(c is d)
#true

l1=[1,2,3]
l2=[1,2,3]
print(l1 is l2)
#false

a='hello-world'
b='hello-world'
print(a is b)

# identity operator only tells whether they belong to same memory location or not

#MEMBERSHIP OPERATOR
print("MEMBERSHIP OPERATOR : tells about the membership")
a="hello"
print("h"in a)
#true
x={1,2,3,4}
print(1 in x)
print("hahaha")

x=[1,2,3,4]
print(5 in x)

print("identity operator can be used as 'is' and 'is not' ")