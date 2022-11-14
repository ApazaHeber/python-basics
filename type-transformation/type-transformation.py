# Dynamically changing the type data
name = 'heber'
print(type(name))

name = 12
print(type(name))

name = True
print(type(name))

age = 12
# We implicitly transform with 'str' function
print('My age is ' + str(age))

#automatically transforms it
print(f"My age is {age}")

# 'input' function always give us a string data
age = input('What is your age: ')
print(type(age))

#transform to int
age = int(age)
print(type(age))

age += 10
print(f"My age is {age}")

#Doest'n transform a string to int 


