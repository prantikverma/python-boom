#STRING OPERATIONS
print("STRING OPERATIONS IN PYTHON :")
print("""1.arithmetic operations
2. relational operations
3. logical operations
4. membership operations
5. loops on strings
\n""")

print("1.arithmetic operations")
print("a. concatenation that is adding {+} two strings")
print("b. repetition or multiplication that is multiplying {*} two strings")

#string concatenation

a="hello"
b="world"
print(a+b)
#helloworld

print("hii"+" sir")
#hii sir

# string multiplication or repetition

print(a*2)
#hellohello
print("*-"*20)

print("2. relational operations")
print("a. equality operator (==)")
print("b. not equal operator (!=)")
print("c. greater than operator (>)")
print("d. less than operator (<)")

#equality operator (==)
a="hello"
b="world"

print(a==b)
#false

print(a=="hello")
#true

print(a!=b)
#true

print("mumbai">"delhi")
#false
#comparison is done on the basis of ascii values of the characters in the string that is lexiographhically
#m comes before p

print("goa"<"kolkata")
#true cause k comes after g

print("hello">"hell")
#true

print("kolkata"<"Kolkata")
#false cause capital letter comes first

print("\nLOGICAL OPERATORS")

print("hello" and "world")
#world ....mllb baad wala true

print("hello" or "world")
#hello ....mllb phle wala true 

print(""and "world")
#''

print("" or "world")
#world

print(not"hello")
#false

print(not"")
#true

#python assumes empty string as false and non empty string as true

#LOOPS ON STRINGS
greet="hello world"
for i in greet:
    print(i)

for i in greet[2:4]:
    print(i)
#l
#l

 #MEMBERSHIP OPERATORS
print("hello" in greet) 
#true

print('h' in greet)  
# true

print('H' in greet)
# false

print('hello' not in greet)
# false

print('@' not in greet)
#true