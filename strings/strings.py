name = 'heber'
last_name = 'apaza'
print(name)
print(last_name)

full_name = name + ' ' + last_name # Concatenacion 

print(full_name)

quote = "I'm heber"

print(quote)

quote2 = 'she said "hello" '
print(quote2)

# CONCATENATION A way to use concatenation 
template = 'Hello, my name is ' + name + ' and my last name is ' + last_name 
print(template)

#other way to use concatenation
template2 = 'Hello, my name is {} and my last name is {}.'.format(name, last_name)
print(template2)

# the most use way to concatenation
template3 = f'Hello, my name is {name} and my last name is {last_name}'
print(template3)
