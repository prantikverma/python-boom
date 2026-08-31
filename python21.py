#BUILT IN FUNCTIONS

#1. print function
print("print function done")

#2. input function
i_p=input("enter any input:")

# 3. type function
print((type(i_p)))

# 4. int , float ,bool ,str ,list ,tuple ,etc

i_p=int(input("enter the input :"))
print(type(i_p))

# 5. abs function

i=1.2
print(abs(i))
#1.2

j=4
print(abs(j))
#4

k=-2
print(abs(k))
#2

# 6. pow function
print(pow(2,3))
#8

# 7. min/max function

print("syntax : min(iterable)")
print("where iterable = list tuple set int")

print(min({1,2,3,4,5,6,7,8,9,0,}))

print(min((1,2,3,4,)))

print(max([1,2,3,4,5,6,7,9,]))

print(min("kolkata"))

print(max("kolkata"))

# round function

pie=22/7
print(pie)
print(round(pie))
#round off value is 3
print(round(4.9))
print(round(4.5))
#4 is the answer
print(round(4.51))
#5
print(round(4.50))
#4

#print round off value to fixed digits
print(round(pie,3))
#value got is 3.143

#9. divmod function
print("divmod(x,y)=(x//y,x%y)")
# // is integer division
# % is modulus operator

print(divmod(5,2))
#(2,1)

# 10. bin/oct/hex function

print(bin(10))
print(oct(10))
print(hex(10))

# 11. id function
#describes the address of memory
a=10
print(id(a))

# 12. ord function
#to get ascii code of any character

print(ord('a'))
print(ord("A"))

# 13. len function tells about the length of string tuple set list

print(len((1,2,3,4,)))
#4

#14. sum function
#sum(iterables)
print(sum({1,2,3}))
#6

#15. help function
# to read the documentation of any funtion
b=help('print')
print(b)
 