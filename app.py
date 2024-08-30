

# ## variable with type 
# print ("hello world")
# name ="owais yousuf" ##str
# age=34               ## int
# height=5.56          ## float
# married=True         ## boolean

# print(type (name), name)
# print(type (age), age)
# print(type (height), height)
# print(type (married), married)

# ## operator
# # 1 arithmetic operator (+,-,/,*,%,**)
# a:int =10
# b:int =5

# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)
# print(a%b)
# print(a**b)

# #relation/comparison operator (== != <> <= >= )
# print(a==b) #false
# print(a!=b) #true
# print(a<b) #false
# print(a<=b) #false
# print(a>b)  #true
# print(a>=b) #true

# assignment operator (= += -= /= *= %= **=)

# a += 10
# # a -= 5
# # a /= 2
# a *= 3
# a %= 3
# print (a)

#logical operator (not , and , or)

#type conversion (automatically conversion  and type casting)

# c:int=2
# d: int=4
# sum = (c+d)
# print(sum) #automatically conversion

# c :str="2"
# d :int=4 
# sum = (c+d) #error because string is not sum in int value

# c :str=int("2")
# d :int=4 
# sum = (2+4) 
# print(sum) #no error because i convert str to int using type casting

#input method in python

# input("enter your name") #out put owais 

# name= input ("enter your name") #input store in a variable
# print ("my name is :", name)
# age = input("enter you age ") #rec date form user in int value but i want to store value in str
age = str(input("enter you age ")) #rec date form user in int value but convert and store in str value
print(type(age) ,"my age is " , age)

