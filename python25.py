#editing and deleting strings in python

#editing strings

c="hello"
print('c[0]="h" is not possible')
#c[0]="H"
#TypeError: 'str' object does not support item assignment
#string do not allow item assignment, they are immutable
#string dont allow editing
print("string are immutable datatype")

c="WORLD"
print(c)
print("reassignment can be done into string but not editing")

#SIMILARLY NOTHING IN STRING CAN BE ADDED
#c[5]="!"
print('c[5]="!" is not possible in python')
#TypeError: 'str' object does not support item assignment
#not possible to add anything into string

#DELETION OF STRING
d="pglu"
#del d[0]
# not possible to delete any character from string
#mutuation not allowed in string

#del d[:3:2]
print("part od string cant be deleted but whole string can be deleted")