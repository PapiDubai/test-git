# name = ()

# def greet_user(username):
#     """Display a simple greeting."""
#     print("Hello, " + username.title() + "!")

# greet_user('sarah')


# def display_message():
#     """Display a message"""
#     print('Todos me pelan la punta de la ve...')

# display_message()


# def favorite_book(user):
#     """Display a message with my favorite book"""
#     print('Hello,  my favorite book is ' + user.title() + "!")

# favorite_book('Harry Potter & The Order Of The Phoenix')

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('Pitbull','Henny')

# def describe_car(make_type, model_type):
#     """Display information about car"""
#     print("\nI have a fast " + make_type + ".")
#     print("My " + make_type + " is a fast af " + model_type.title() + "!")

# describe_car('BMW', '335i')
# describe_car('Mercedez', 'E65 AMG')


#RETURNING A SAMPLE VALUE

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = first_name + ' '+ middle_name +' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# def build_peron(first_name, last_name, age=' '):
#     """Return a dictionary of insformation about a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_peron('jimi', 'hendrix', age=27)
# print(musician)

# def get_formatted_name(first_name, last_name):
#      """Return a full name, neatly formatted."""
#      full_name = first_name + ' ' + last_name
#      return full_name.title()

# This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

    # formatted_name = get_formatted_name(f_name, l_name)
    # print("\nHello, " + formatted_name + "!")

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

unprinted_designs = ['iphone case', 'robot pendant', 'dedocahedron']
completed_models = []

#Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_designs = unprinted_designs.pop()
