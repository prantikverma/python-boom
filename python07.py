#keywords in python
#33 keywords in python
#keywords are reserved words in python that have special meaning and cannot be used as identifiers (variable names, function names, etc.)
#keywords are used to define the syntax and structure of the python language
#keywords are case-sensitive and must be written in lowercase
#keywords cannot be used as variable names, function names, or any other identifiers

import keyword

print(keyword.kwlist)

#identifiers in python
#identifiers are the names given to variables, functions, classes, modules etc.
#identifiers can contain letters, digits, and underscores
#identifiers cannot start with a digit
#identifiers are case-sensitive

print("guidelines to name an identifier\n")
print("1. Identifiers can contain letters, digits, and underscores.")
print("2. Identifiers cannot start with a digit.")
print("3. Identifiers are case-sensitive.")
print("4. Identifiers cannot be keywords.")
print("5. Identifiers should be descriptive and meaningful.")
print("6. Identifiers should not contain special characters or spaces.")
print("7. Identifiers can only start with letters or underscore")

name="vincenzo"#valid
_=10#valid
#2_id=12  this is invalid because it starts with a digit
first_name="paras"#valid
last_name="sir"#valid

