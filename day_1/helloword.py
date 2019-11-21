# checking the python version
import sys
print('*'*25, 'Question 1', '*'*25)
print('The python version of this system is : ', sys.version[:6])


num_1 = 8
num_2 = 2
print('First number is : ', num_1)
print('Second number is : ', num_2)

# computing different mathematical expressions
print('*'*25, 'Question 2', '*'*25)

print('addition(+)', num_1 + num_2)
print('substraction(-)', num_2 - num_1)
print('multiplication(*)', num_1 * num_2)
print('modulus(%)', num_1 % num_2)
print('division(/)', num_1 / num_2)
print('exponential(**)', num_1 ** num_2)
print('floor division operator(//)', num_1 // num_2)

# working with strings
print('*'*25, 'Question 3', '*'*25)

first_name = 'Kedar'
last_name = 'Kanel'
country = 'Nepal'
msg = 'I am enjoying 30 days of python'

print('My name is ', first_name, last_name, '. I am from ', country, '. ', msg)

# working with data types
print('*'*25, 'Question 4', '*'*25)

print('Data type of 10 is : ', type(10))
print('Data type of 9.8 is : ', type(9.8))
print('Data type of 3.14 is : ', type(3.14))
print('Data type of 4 - 4j is : ', type(4-4j))
print("Data type of ['Asabeneh', 'Python', 'Finland'] is : ",
      type(['Asabeneh', 'Python', 'Finland']))

print('Data type of first_name is : ', type(first_name))
print('Data type of last_name is : ', type(last_name))
print('Data type of country is : ', type(country))


a = 1
b = 1, 2, 3
x = a, b
print(type(x))
