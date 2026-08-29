#for loop in python
print("""for loop syntax:
for variable in range(start,end+1):
    code
\n""")

#range function
seq=range(1,10)
print(list(seq))
#10 is excluded

print(""" syntX FOR range function:
range (start,stop,step)""")

#demo1
demo1=range(5)
#starting is by fault "0" and end is 5-1=4
print(demo1)
#range(0,5) will  be printed
print(tuple(demo1))
#(0,1,2,3,4) willl be printed

demo2=range(0,21,2)
#step included
print(list(demo2))

#negative steps
demo3=range(10,-1,-2)
print(list(demo3))

#sequence= order

#for loop iterates upon sequence and range function

#iteration upon range
for i in range (0,11):
    print(i)
    #printing 0 to 10 

#iteration in sequence
for i in ["amritsar","balwakot","chandigarh",'dehradoon','euthopia']:
    print (i)

for i in "india":
    print(i)

for i in (1,2,3,4,5,6,7):
    print(i)

print("sequence here represents string, list, tuple, set, dictionary\n")
#in dictionary its different

print("use for loop if u know the exact number of iterations \nif u dont know the number of iteratons then use while loop for sure ")