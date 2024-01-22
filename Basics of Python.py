#Strings
# a="sushant"
# for i in a:
#     print(i,end="") 
#Concatenation +
# x="every"+"day"
# print(x)
#Replication *
# a=3*"Sushant"
# print(a)


#getting value from user
#1 x=int(input("Enter a number"))
# y=int(input("Enter 2 number"))
# a=x+y
# print(a)
#############################
#2 result=eval(input("Enter a exp"))
# print(result)


#Diffrent ways to print your code
#1 hello="Starting a new journey today"
# print("at vdoit techonologies ltd {}".format('hello'))
#2 a="Welcome {},you are sitting in {}".format("sushant",'building')
# print(a)


#F-strings
# user_name=input("What is your name? ")
# print(f"Hello {user_name},welcome to python!")

#2 name="sushant"
# mydict={'name':'sushant'}
# print(f'my name is {mydict["name"]}')

#3 print(f'Ten time 10 is {10*10}')
#>>>>>Lists
#num=[25,26,58,545,45]
# print(num[0])
# print(num[2:])
# print(num[-3])
#values=[9.6,"sushant",26]
#print(values)
# names=["A","b","C","d"]
# mim=[num,names]
# print(mim)
# num.append(87)
# print(num)
# print(mim)
# names.insert(2,100)
# print(names)
# del num[2:]
# print(num)
# num.extend([23,56,65,44])
# print(num)
# num.sort()
# print(num)

####Tuple
# a=(34,54,53,67,"abcds",58.5)
# print(a)
# print(type(a))

##Sets
# a={10,20,45,'abcd',4.6}
# print(a)
# print(type(a))

##Dictionary
#1 data={1:"Sy",2:"by",3:'sd'}
# #print(data[2])
# print(data.get(5,'Not Found'))

#2 keys=["Sush","Vats","Aak"]
# values=["Py",'Js','C']
# data=dict(zip(keys,values))
# print(data)
# print(data['Sush'])
# data['Monu']='Cs'
# print(data)

##example3
# prog={'JS':'atom','Cs':'Vs','python':['pycharm','sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
# print(prog)
# print(prog['JS'])
# print(prog["python"][1])
# print(prog['Java'])

#####################Files
# An attempt to open a folder name
# results in a permission error.
# import os
# directory_location=os.listdir("D:/Week_1(Python)/Data")
# # file = open("D:\\Week_1(Python)\\Data")

# for file in directory_location:
#     print((file))

# f=open('text.txt','r')
# print(f.mode)
# f.close()
##################Not working##

#for loop

# a=8
# b=18
# for i in range(b,a,-2):
#     print(i)


# for i in range(1,22):
#     if i%5!=0:
#         print(i)

# i=1
# while i<=5:
#     print('hello ',end="")
#     j=1
#     while j<=4:
#         print('world ',end="")
#         j=j+1

#     i=i+1
    # print()



##normal list creation
# lst1=[]
# for i in range(20):
#     if(i%2==0):
#         lst1.append(i)
#     else:
#         lst1.append("Invalid") 

# print(lst1)

##1 List comprehension
# list1=[i+1 for i in range(20) if i%2==0 if i%3==0]
# print(list1)

##2 
# lst2= [i if i%2==0 else "Invalid" for i in range(20)]
# print(lst2)


##Functions

# def add():
#     x=45
#     y=32
#     c= x+y
#     print(c)
# add()    


# def sub():
#     g=90
#     y=87
#     r=g-y
#     print(r)
# sub()   

# def add(y):
#     x=34
#     print(y+x)

# add(20)    

# def add(y):
#     x=10.3455
#     print(x+y)
#     print(f"Formated output {x+y:5.2f}")

# add(20)    


# """Q2 To check if the first number and last number of a list are same"""
# #create a list
# list1=[int(input("Enter the values in list1 "))]
# #use the index value of the numbers to check if equal or not
# first_num=list1[0]
# last_num=list1[-1]

# #condition to check
# if first_num==last_num:
#     print("Equal")
# else:
#     print("Not Equal")  


# # Initialising string
# ini_string1 = input("Enter the String")
 
# # Initialising number of characters to be removed
 
# # Printing initial string
# print("Initial String", ini_string1)
 
# # Removing n characters from a string
# # This argument count length from zero
# # So length to be stripped is passed n-1
# res = ini_string1[6:]
 
# # Printing resultant string
# print("Resultant String", res)

#Initialising string
# ini_string=input("Enter the String = ")
# x=int(input("Enter a number"))
# print("Initial String",ini_string)

# #Now removing n characters from the string counting length from 0
# res=ini_string[x:]

# print("Resultant String",res)


# word = input("enter first number")
# n = int(input("enter number"))
# print('Original string:', word)
# x = word[n:]
# print('New string:', x)



# ini_string1 = 'sushantsingh07'
# # Initialising number of characters to be removed
# n=5
# print("Initial String", ini_string1)
 
# # Removing n characters from string using
# res = ''
# for i in range(0, len(ini_string1)):
#     if i >= n:
#         res = res + ini_string1[i]
 
# # Printing resultant string
# print("Resultant String", res)




