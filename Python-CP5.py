cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())



requested_topping = 'mushrooms'

if requested_topping != 'anchiovis':
    print("Hold the anchiovis!")

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age = 19
if age >= 18:
    print("You are old enough to buy ciggarets!")
    print("Have you bought some yet?")

    age = 17
if age >= 18:
    print("You are old enough to buy ciggarets!")
    print("Have you bought some yet?")
else:
    print("Sorry, you are too young to buy cigarretes.")
    print("Please buy some as soon as you turn 18!")

age = 75

if age < 4:
    price = 0
    # print("Your admission cost is $0.")
elif age < 18:
    price = 5
    # print("your admission cost is $5.")
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
    # print("Your admission cost is $10.")

print("Your admission cost is $" + str(price) + ".")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding" + requested_topping + ".")

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# elif 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# elif 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza!")


#This lets you print when there is a value for either x or y
x = 0
y = 1

if x:
    print("howdy")
elif y:
    print("Hello from here")