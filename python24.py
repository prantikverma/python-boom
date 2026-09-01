#ASSESSING SUBSTRINGS IN PYTHON
print("in this file we will learn indexing and slicing")

#indexing
c="hello"
print(c)

print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])
#print(c[5]) error out of range

print("""types of indexing 
1. positive indexing
2.negative indexing""")

print(c[3])
#l

print(c[-1])
#o
print(c[-5])
#h

#slicing
print("slicing : extracting multiple charcters from string")

greet="hello world"
print(greet[0:5])
#index 0 to index 5-1=4
#hello

print(greet[0:])
#hello world

print(greet[1:])
#ello world

print(greet[:5])
#hello

print(greet[:])
#hello world

print(greet[2:6:2])
#lo

print(greet[:5:2])
#hlo

print(greet[0:8:3])
#hlw

#negative steeping cant be used into positive indexing 
print(greet)






