# a = [1,3,5]
# b = [2,4,6]
# c = [7,8,9]
# # print(a + b + c)
# print(a)
# print(b)
# print(c)

# a = "dress club "
# b = "ahsan ghani"
# print (a+ b)



# x = 45
# y = 34
# z = 26
# print(x  < y)
# print(x>z and y>x)
# a = 12
# b = "ahsan"
# c = 23.4
# a =["ahsan",12,23]
# a_1 = (12,13,41)
# a_2={"ahsan": 13,"khalid":45,"sami": 45}
# print(a)
# print(a_1)
# print(a_2)# 
# print(a_2["sami"])



# person_A_name =input("Enter your name: ")
# person_A_age = int(input("Enter your age: "))

# person_B_name = input("Enter your name:")
# person_B_age = int(input("Enter your age:"))

# if person_A_age >person_B_age:
#     print(person_A_name,"is older than",person_B_name)
# else:
#     print(person_A_name,"is younger than",person_B_name)
   

# name = input("Hello Sangi! What is your name: ")
# weight = int(input("Enter your weight in kg: "))
# height = float(input("Enter your height in cm: "))
# height = height / 100

# bmi = weight / (height/100)**2

# print("Hello", name, "your BMI is", bmi)

# if(bmi < 18.5):
#     print("You are underweight, ghr walay khana nahi dete?")
# elif(bmi >= 18.5 and bmi < 24.9):
#     print("Your weight is normal, keep it up")
# elif(bmi >= 24.9 and bmi < 29.9):
#     print("You are overweight, tobah tobah")
# else:
#     print("You are obese, tobah tobah tobah, tobah")



# names = ["ahsan", "abdullah","Esha","Nafees"]
# print(names)
# names[2] = "Esha Khan"
# print(names)


# cars ={"Brand": "Toyota","Model": "Corolla", "Year": 2020}
# print(cars)
# cars["Year"]=2026
# print(cars["Year"])



# foods = ["Pizza", "Burger", "Pasta", "Salad"]
# for food in foods:
#     print(food)
# i=18
# for i in range(1,15):
#     print(i)


# i=0
# while i < 10:
#     print(i)
#     i+= 1



# for letter in "ahsan swati":
#     if letter =="w":
#         continue
#     print(letter)





 #### Nested loops 

## Nested  for loop



# colors = [ "red", "green", "blue"]
# items =[ "pen", "copy", "pencil"]
# for color in colors:
#     for item in items:
#         print(color, item)



# names = ["ahsan", "abdullah","Esha","Nafees"]
# subjects = ["Math", "computer Science", "english ","urdu"]
# for name in names:
#     for subject in subjects:
#         print (subject ,"is Studing in", name) 



## Nested while loop



# i = 0 
# while i < 3:
#     j=0
#     while j<3:
#         print(i,j)
#         j+=1
#     i+=1

# print("Hello World")
# print("Ahsan ")


#for in inside while loop

# i = 0
# while i<4:
#     for j in range (1,4):
#         print(i,j)

#     i+=1  


# while loop inside for loop
# for i in range (5):
#     j = 0
#     while j<4:
#         print (i ,j)
#         j+=1





##function      
# def ahsan_ghani():
#     print ("Hello Ahsan Ghani ! How are you doing today?")
# ahsan_ghani()
        

# def aoa(name = "mery piyary dost"):
#     print(f"asamualkum {name} ! How are you doing today?")

# aoa()



# def add_numbers(num1, num2):
#     print("the Sum of these two number is!",num1+num2)

# add_numbers(12,14)




#return statement in function
# def square(num):
#     return num*num
# print (square(4))
    





#recursion function
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n* factorial (n-1)
# print (factorial(6))
     



# #lambda function
# x = lambda i: i*3
# print(x(2))




