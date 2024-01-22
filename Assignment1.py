"""Q1 To print if the product of two integers is less than or equal to 1000,else print there sum!!"""
#Taking two integers as num1 & num2
num1=int(input("Enter the first number = ")) #input is used to take command from the user
num2=int(input("Enter the second number = ")) 
product=num1*num2
#Now we write condition to check if the product is less than 1000 or not
if product<=1000:
    print("The product of num1 & num2 is:",product)

else:
     #if product is greater than 1000 then calculate sum
    print("The sum is:",num1+num2) 



"""Q2 To check if the first number and last number of a list are same"""
#create a list
list=[12,19,36,47,58,46,25,78,12]
#use the index value of the numbers to check if equal or not
first_num=list[0]
last_num=list[-1]

#condition to check
if first_num==last_num:
    print("Equal")
else:
    print("Not Equal")    



"""Q3 Removing first n characters from a an input string"""

#Initialising string
ini_string1 = input("Enter the String")
print("Initial String", ini_string1)
 
# Removing n characters from a string using the index value of characters of string
res = ini_string1[6:]
 
# Printing resultant string
print("Resultant String", res)

"""Another solution"""

#Initialising string
ini_string=input("Enter the String = ")
x=int(input("Enter a number"))
print("Initial String",ini_string)

#Now removing n characters from the string counting length from 0
res=ini_string[x:]

print("Resultant String",res)



"""Q4 Return the count of a given substring from a string """
strings = ["Sushant", "singh", "at","vdoit"]
char_to_count = 'a'
total_count = sum(string.count(char_to_count) for string in strings)
print(total_count)




    