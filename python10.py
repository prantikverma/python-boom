#literals in python

print("""literals : raw data in the variable""")
print("4 types of literals")
print("""1.numeric
2.string
3.boolean
4.special""")

#numeric literals
a=10
b=0b1010
c=0o12
d=0xA
print(a,b,c,d)
#float literal
float_a=10.5
print(float_a)
float_b=1.5e2
#float_b=150.0=1.5*10^2
print(float_b)
float_c=1.5e-2
#float_c=0.015=1.5*10^-2
print(float_c)
#complex literal
complex_a=1+2j
print(complex_a)
print("complex_a real part :",complex_a.real)
print("complex_a imaginary part :",complex_a.imag)

#string literals
print("string literals are sequence of characters enclosed in single or double quotes or triple quotes")
string_a="hello"
print(string_a)
string_b='hii'
print(string_b)
character='a'
print(character)
mutliline_string="""this is a
multiline string"""
print(mutliline_string)
unicode_string=u"\U0001f600\U0001f601\U0001f602"
#EMOJI unicode string
print(unicode_string)
raw_string=r"this is a \n  raw string"
print(raw_string)

#boolean literals
print("boolean literals are True and False")
boolean_a=True
boolean_b=False
print(boolean_a)
print(boolean_b)
print(boolean_a+4)
#true=1
#1+4=5
print(boolean_b+10)
#false=0
#0+10=10

#special literals
a=None
print(a)
#None means absense of anything

