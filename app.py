

# #chapter 1 variable with type 

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
# age = str(input("enter you age ")) #rec date form user in int value but convert and store in str value
# print(type(age) ,"my age is " , age)


#chapter 2 string and if elif else statement

#string
# a="my name is owais yousuf and i learn python in piaic" #this is one line statement
# print(a)

# a="my name is owais yousuf \ni learn python in piaic" #this is next line statement 
# print(a)

# a="my name is owais yousuf \ti learn python in piaic" #this is creat tab spaces  
# print(a)

#lenght of strings
 # a="owais"
# b="yousuf"
# c= a+b
# print(a, len(a))
# print(b, len(b))
# print (c, len(c)) #check variable lenght and give you to total charcter in a string

#index of string
# a= "hello world"
# print(a[0]) #single index
# print(a[0:6]) # 0 to 5 index always give one index extra
# print(a[6:])  # 6 to end index
# print(a[:8])  # start to 8 index

#string Function

#end with function
# a = "my name is owais i am learning python"
# print(a.endswith("is")) #string end with is result false
# print(a.endswith("on")) #string end with on result true

#capitalize function
# a = "my name is owais i am learning python"
# print(a.capitalize()) #capitalize first word

# #replace function
# a = "my name is owais i am learning python"
# print (a.replace("s", "e")) # replace s into e and copy the string not change in original string
# print (a.replace("python", "typescript")) # replace python into typescript and copy the string not change in original string

# # #count function
# a = "my name is owais i am learning python"
# print(a.count("i")) #count the number of i in string 

# if -elif-else statement

# age =17
# if (age >=18) :
#   print("you are adult")
# else: print("you are kid")
# #if age is less than 18 print you are kid and if age in 18 or 18 above print you are adult

# color=input("enter your color ")
# if (color=="red"):
#   print("stop")
# elif(color == "yellow"):
#   print("ready")
# elif(color == "green"):
#   print("go")
# else:"light is broken"  

