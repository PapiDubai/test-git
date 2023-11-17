# cars = ["audi", "ferrari", "ford focus", "toyota sienna hybrid"]
# groceries = ['apples', 'oragenges', 'bananas']

# def car_adder(thing_to_add, target_list):
#     # cars.append(car_to_add)
#     if thing_to_add[0].lower() in 'abcde':
#         print("This car starts with A-G")
#         target_list.append(thing_to_add)
#     else:
#         print("This car starts with H-Z and we are not allowing it in our club")


# car_adder("Bmw", cars)
# car_adder("Honda", cars)
# car_adder("Cinnamon", groceries)
# car_adder("apples", groceries)

# print(cars)
# print(groceries)

def addTwo(num):
    return num + 2

def addThree(num):
    return num + 3

# print(addThree(addTwo(5)))

def namePrinter(first, last, middle=''):
    return f"The name's {last}, {first} {middle} {last}."

# print(namePrinter("James", "Bond", "Freddy"))

def giveMeMyGroceries(things_to_add):
    sports_dic = {'soccer': ['Manchester City', 'Liverpool'],
                    'basketball': 'Cavaliers',
                    'baseball': 'Marlins'}
    sports_dic['wrestling'] = things_to_add
    return sports_dic

print(giveMeMyGroceries(['Dan Gable', 'The Rock', 'The Undertaker']))