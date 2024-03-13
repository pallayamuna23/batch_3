#!Eg:3
#?Take values of length and breadth of a
#?from user and check if it is square or not.
'''
length=int(input())
breadth=int(input())
if length==breadth:
    print("its a square")
else:
    print("its no square")
'''
#!Eg:4
#python program to check whether the
#given integer is a multiple of both 5 and 7
'''
n=int(input("enter the number:"))
if n%5==0 and n%7==0:
   print("yes")
else:
   print("no") 
'''
#!Eg:5
#write a program to accept the cost price of a bike and display the
#roa tax to be paid
#according to the following criteria:
#cost price(in Rs)                   tax
#>100000                             15%+discount 6%
#<100000                             5%
'''
price=int(input("enter the  price:"))
amount=0
if price>=100000:
    discount=price*(6/100)
    value=price-discount
    amount=value*(15/100)
    print(value+amount)
else:
    tax=price*(5/100)
    total=price+tax
    print("The onroad cost of  bike is:",total)
'''
#if elif
'''
Eg:1
a=7
b=9
c=4
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("C is greater")
'''
# A school has foolowing rules for grading system:
#a. below 25 -F
#b. 25 to 45 -E
#c. 45 to 50 -D
#d. 50 to 60 -C
#e. 60 to 80 -B
#f. above 80 -A
#ask user to enter marks and print the corresponding grade.
'''
mark=int(input("enter mark:"))
if mark>=80 and mark<100:
   print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>45 and mark<50:
    print("D")
elif mark>=25 and mark<45:
    print("E")
elif mark>=0 and mark<25:
    print("F")
else:
    print("fail")

#!-->short hand if else
#Eg:1
a=19
b=34
if a>b:
    print("A")
else:
        print("B")
#?-->using short hand if else
# rules
# 1.statement inside the if condition have to be present at first
# 2.elif cannot be used in short hand if else
# 3.always it have to end with else
print("A") if a>b else print("B")
'''
#! code to check the given char is vowel or consonent
'''
char=input("enter the char:")
if char=='a' or char=='i' or char=='o' or char=='u':
    print("is a vowel")
else:
    print("its consonent")
'''
'''
#or
char=input("enter the char:")
str1="aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonent")
    
 #!short hand if else
char=input("enter the char:")
str1="aeiouAEIOU"
print("vowels") if char in str1 else print("consonent")
'''
#!-->elif ladder using short hand if else

'''
a=8
b=5
c=6
print("A is greater") if a>b and a>c else print("Bis greater") if b>a and b>c else print("C is greater")
'''
#--->looping
#looping can be implemented using
#for loop
#while loop
#--->for loop
#for loop used to iteration,if we know the number of times the loop have to run
#it is used to iterate the iterables eg(string,list,tuple,etc...)
#todo-->syntax for loop
#for syntax in c
#for(i=0;i<10;i++){
#   print("hello");
#   }
#!for syntax in python
#for user defined variable in range(start,end,step):
#    statement
#    statement
#    statement
'''
#eg:1 for loop
#to print values from 1 to 10 using for loop
for i in range(0,10):    #(n,n-1)
    print(i)

#eg:2
for val in range(20,50,5):
    print(val)

#eg:3
#to decrement the value
for val in range(10,0,-1):
    print(val)
    '
#eg:4
#print the output of 7th multiplication table from 21 to 43
#method-1
for val in range(1 , 10+1):
       # print('7','X',val,'=',val*7)
#method-2
        #ans="7 x {}={}"
       #print(ans.format(val,val*7))
#method-3
       print(f"7 x {val}={val*7}")
          
'''
#eg:5
#break statement-->used to terminate the loop or stop the loop
#for val in range(1,10):
  # print(val)
   #if val ==6: 
    # break

 #  if val ==6: 
  #   break
   #print(val)
'''
#continue
#eg:1
for val in range(1,10):
    if val==6:
          continue
    print(val)

  #practise problems
  #print the even number 20 to 40
  
for val in range(20,40):
    if val%2==0:
       print(val)
       '''
#!--->while loop
#while loop is used when we do not know the number of times the loop have to run
#to iterate the non iterable while loop is used
#todo syntax
#intialiasation
#while condition:
#statement
#incre or decre
#eg:1
i=0
while i<11:
    print(i)
    i+=1




















































    
          
          
