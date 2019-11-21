# Day 2: 30 Days of python programming

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
variable_type = {first_name: type(first_name), last_name: type(last_name), full_name: type(
    full_name), country: type(country), city: type(city), age: type(age), year: type(year),
    is_married: type(is_married), is_light_on: type(is_light_on), is_true: type(is_true)}
print(variable_type)

len_first_name = len(first_name)
len_last_name = len(last_name)

print('Length of first name is : ', len_first_name)
print('Length of last name in : ', len_last_name)

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# finding the area and circumference of a circle
radius = 30
area_of_circle = 3.14 * radius * radius
