#STRING FUNCTIONS IN PYTHON

print("common functions in strings are -->")
print("""1. len() function
2. min() function
3. max() function
4. sorted() function
\n""")

print(min("prantik"))
#a

a=min('hello','HELLO')
print(a)
#HELLO

print(max("prantik"))
#t

print(len("hello world"))
#11

print(max("delhi","agra"))
#delhi

print(sorted("hello"))
#['e', 'h', 'l', 'l', 'o']  
#sorted function returns a list of characters in the string in ascending order

print(sorted("hello",reverse=True))
#sorted in descending order