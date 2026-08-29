#FINALLY FOR LOOP IS HERE 
print("welcoming for loop into target")
#FOR LOOOP HAVE MORE TIME COMPLEXITY
print("""printing a pattern::
*
**
***
****
*****\n""")

rows=int(input("enter the number of rows :"))

for i in range(1,rows + 1):
    for j in range(0,i):
        print("*",end=" ")
    print("")