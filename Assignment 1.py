'''
	NAME:: LUNGADE KIRAN
	PRACTICAL NO.:: 01
	TITLE:: PYTHON CODE FOR PRIME, SWAP, LEAP YEAR, FIBONACCI
'''

#1.   ****************      Prime Number code      ********************
num= int(input("Enter the number:: "))

if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


#2.   ***************    Swapping of 2 number with out using 3rd variable     ***********
num1=int(input("Enter first number:: "))
num2=int(input("Enter second number:: "))
(num1,num2)=(num2,num1)
print("First number after swapping:: ")
print(num1)
print("Second number after swapping:: ")
print(num2)


#3.  *****************     Leap year code    *******************
year=int(input("Enter year:: "))
if(year%4==0 and year%100!=0 or year%400==0):
    print(year," is leap year..")
else:
    print(year," is not leap year..")


#  ****************   4. Fibonacci Series   **************************
n1 = int(input("Enter 1st number:: "))
n2 = int(input("Enter 2nd number:: "))
count = 0

nterms = int(input("How many terms? "))

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
