#write a program for hello world.
print("hello world")
print(f"Hello {'world'}") #string formatting

#write a program for add two numbers.
a=int(input("Enter a number1:")) 
b=int(input("Enter a number2:"))                      #using + operator
print("the sum of {} and {} is".format(a,b),a+b)

def add():
    a=int(input("Enter a number1:"))
    b=int(input("Enter a number2:"))                 #using function
    print("the sum of {} and {} is".format(a,b),a+b)
add()   

a = float(input("Enter the First Value  = "))
b = float(input("Enter the second Value = "))         #without using + operator
numList = [a,b]
result = sum(numList)
print(result)

x = float(input("Enter the First Value  = "))
y = float(input("Enter the second Value = "))          #using lambda function
result = lambda x, y: x + y
print(result(x,y))

#write a program for subtraction of two numbers.
a=int(input("Enter a number1:"))
b=int(input("Enter a number2:"))                            #using - operator
print("the subtraction of {} and {} is".format(a,b),a-b)

def sub():
    a=int(input("Enter a number1:"))
    b=int(input("Enter a number2:"))                              #using function
    print("the subtraction of {} and {} is".format(a,b),a-b)
sub()

#write a program for multiplication of two numbers.
a=int(input("Enter a number1:"))
b=int(input("Enter a number2:"))                                 #using * operator
print("the multiplication of {} and {} is".format(a,b),a*b)

def mul():
    a=int(input("Enter a number1:")) 
    b=int(input("Enter a number2:"))                             #using function
    print("the multiplication of {} and {} is".format(a,b),a*b)
mul()

#write a program for the given number is positive,negative and zero.
num=int(input("Enter a number:"))
if(num>0):
    print("{} is a positive number".format(num))
elif(num<0):
    print("{} is a negative number".format(num))
else:
    print("you entered number is zero")

#write a program for the given number is even or odd.
num=int(input("Enter a number:"))
if(num%2==0):
    print("{} is a even number".format(num))
else:
    print("{} is a odd number".format(num))

#write a program for the given year is leap year or not.
year=int(input("Enter the year:"))
if(year%4==0 or year%400==0):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))

#wirte a program for calender.
import calendar
year=int(input("Enter the year:"))
month=int(input("Enter the month:"))
print(calendar.month(year,month))

#write a program for cube of a given number.
num=int(input("Enter a number:"))
cube=num**3
print("the cubic of a {} is".format(num),cube)

a = int(input("Please Enter the First value: "))
b = int(input("Please Enter the First value: "))
c = int(input("Please Enter the First value: "))

if (a > b and a > c):
    print("{0} is Greater Than both {1} and {2}". format(a, b, c))
elif (b > a and b > c):
    print("{0} is Greater Than both {1} and {2}". format(b, a, c))
elif (c > a and c > b):
    print("{0} is Greater Than both {1} and {2}". format(c, a, b))
else:
    print("Either any two values or all the three values are equal")



    
