#fizzbuzz
x = int(input())
for i in range(1,x+1):
    if (i%3==0) and (i%5==0):
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
        
 #square pattern       
x= int(input())
for i in  range(x):
    for j in range(x):
        print("*",end=" ")
    print()
    
 #triangle pattrn   
x = int(input())
for i in range(x):
    for j in range(i+1):
      print("*",end=" ")
    print() 
  #diamond pattern  
x= int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()  
for i in range(x-2,-1,-1):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
#using 4 inputs
x= int(input())   
for i in range(x):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()    
        
    
    
    
    
    
    


     
        
