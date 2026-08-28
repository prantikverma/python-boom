print("""using more than 2 conditions 

if 
elif
else\n""")

email_inserted=input("email enter krr :")
pass_inserted=input("password enter krr:")

if (email_inserted=="prantikvermaparas@gmail.com" and pass_inserted=="1234"):
    print("login successful")

elif(email_inserted=="prantikvermaparas@gmail.com" and pass_inserted != "1234"):
    print("password incorrect")
    pass_inserted=input("password wapis likh: ")
    
    if (email_inserted=="prantikvermaparas@gmail.com" and pass_inserted=="1234"):
         print("login successful")
        
    else:
         print("incorrect again")

else:
    print("try again later")



