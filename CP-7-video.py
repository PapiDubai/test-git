# x = 0

# flag = True

# while flag:
#     print(x)
#     x += 1
#     if x > 100:
#         flag = False

while True:
    my_name = input("what is your name? \n")
    if my_name.lower() == 'quit':
        break
    elif my_name.lower()[0] in 'abcdefg':
        print('Please proceed to table One')
    elif my_name.lower()[0] in 'hjklmnop':
        print('Please proceed to table Two')
    elif my_name.lower()[0] in 'qrstuvwxyz':
        print('Please proceed to table Three')


for letter in "Yee Haw Yippee Ki Yay":
    print(letter)