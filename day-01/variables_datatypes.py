print("Hello World!")
x="Ammar"
print("Hello"," ",x)

#Operators
print(45*4)
x=5
print(x is 5)
print(x+4)
print(6%1)
a = 10
b = 3
print(a + b)          
print(a / b)          
print(46 // b)         
print(a % b)          
print(2 ** b)         
print(a >= b)         
print(a != b)        
print(a > 5 and b < 5) 



#Updated input 
x=int(input("Enter a number"))
print(x)
print(x+1)
print(type(x))


# #Updated conditional statements

num=int(input("Enter a number"))
if num %2== 0:
  print("Even")
elif num%2!=0:
  print("Odd")
else:
  print("0")
#Updated Loops    
for i in range(1,6,-2):
    print(i)

##Updated continue and braek 
i=5 
while i<=10:
    if i==7:
        continue
    print(i)   
    if i==10:
        break
        
    i+=1
