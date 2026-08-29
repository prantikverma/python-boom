#BREAK CONTINUE AND PASS
print("we are learning break continue and pass keywords \n")

#break statement 
#break is used in linear search scenerio

print("break statement terminates the loop")

for i in range(1,10):

    if i>=5:
         break
    
    else: 
         print(i)
         i+=1

#continue statement

print("continue statement is used to escape the loop")

for j in range(1,10):
     if j==5:
          continue
          #5 is escaped but other values are continued printing
     print(j)

#pass statement
#pass is like filler if we dont have any logic for now but we will note the logic later
#simply we need time for logic untill then it acts a filler


