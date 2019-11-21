# Day 2: 30 Days of python programming

# all the imports
import keyword
import math

# initializing the variables
first_name = 'Ram'
last_name = 'Bahadur Chhetri'
full_name = first_name + last_name
country = 'Nepal'
city = 'Butwal'
age = 34
year = 2018
is_married = False
is_true = True
is_light_on = False
a, b, c = 2, 3, 4

# creating dictoinary with variable name as key and type of variable as value
variable_type = {first_name: type(first_name), last_name: type(last_name), full_name: type(
    full_name), country: type(country), city: type(city), age: type(age), year: type(year),
    is_married: type(is_married), is_light_on: type(is_light_on), is_true: type(is_true)}
print('*'*50)
print(variable_type)

# comparing the length of first_name and last_name
print('*'*50)
len_first_name = len(first_name)
len_last_name = len(last_name)

print('Length of first name is : ', len_first_name)
print('Length of last name in : ', len_last_name)

# doing some mathmatical operations
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# dictionary with operation name as key and result as value
calculation = {'add': total, 'substract': diff, 'multiply': product, 'divide': division,
               'remainder': remainder, 'exponential': exp, 'floor': floor_division}
print('*'*50)
print(calculation)

# finding the area and circumference of a circle
radius = 30
area_of_circle = math.pi * radius * radius
circum_of_circle = 2 * math.pi * radius

print('*'*50)
print('Area of circle with radius 30 is : ', area_of_circle)
print('Circumference of circle with radius 30 is : ', circum_of_circle)
print('*'*50)

# takes radius as user input
user_input_radius = input('Please input the radius : ')
circle_area = math.pi * user_input_radius * user_input_radius
print('Area of circle with radius ', user_input_radius, 'is : ', circle_area)

first_namee = raw_input('Please enter your first name : ')
last_namee = raw_input('Please enter your last name : ')
countryy = raw_input('Please enter your country : ')
print('Hello ', first_namee, ' ', last_namee,
      'from ', countryy, '. How are you doing? ')

# check the reserved words
print('*'*50)
print('Python reserved keywords are : ', keyword.kwlist)
