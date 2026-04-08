# print('Hi Python!')

# cars = ['audi','subaru','toyota']

# for car in cars:
#     if car == 'bmw':print(car.upper())
#     else:
#         print(car.title())
        
# car = 'audi'
# if car == 'audi':
#  print(False)  
# else:
#     print(True)
    
# print(car)

# age = 22

# if age < 4:
#     prise = 0
# elif age < 18:
#     prise = 29
# else:
#     prise = 40
# print(f"Yor admichion cost in ${prise}")
    
    
    
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20
# print(f"Your admission cost is ${price}.")

# Словарь 

# favorite_languges = {
#     'jim': 'python',
#     'tom': 'c++',
#     'saimuel': 'java',
#     'julia': 'ruby',
# }

# language = favorite_languges['julia'].title()
# print(f"Julia favorite languages {language}")
# print(favorite_languges)

# toyota = {
#     'engine': 1.5,
#     'color': 'blasc',
#     'year': 2026,
# }

# print(toyota['color'].upper())

# toyota['x_position']= 2
# toyota['y_position']= 25
# print(toyota)

# toyota = {}
# toyota['color']= 'green'
# toyota['year']= 2025
# print(toyota)
# del toyota['color']
# print(toyota)

# def user_name(username):
#     print(f"Heloo,{username.title()}!")
    
# user_name('pavel')

# def deskri_pet(animal_tippe,pet_name):
#     print(f"\n In hawe {animal_tippe}")
#     print(f"\n your {animal_tippe} name is {pet_name.title()}")
# deskri_pet('elifant','chugar'
# )

# def get_formated_name(first_name,last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# vusician = get_formated_name("jim","hendriks")
# print(vusician)

def get_formated_name(first_name, last_name, middle_hame = ''):
    if middle_hame:
        full_name = f"{first_name} {middle_hame} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
    
musician = get_formated_name("jim","hendrics")
print(musician)

musician = get_formated_name("jim","hendrics","lee")
print(musician)