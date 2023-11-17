grocery_list = ["apple", "banana","orange","spinach", "kale", "curry", "potatoes", "quiche", "quinoa"]

urgent_groceries = []

for item in grocery_list:
    if item[0] in ['a', 'b', 'c']:
        urgent_groceries.append(item)
    else:
        continue

my_groceries = [item for item in grocery_list if item[0] in ['a', 'b', 'c']]

print(urgent_groceries)
print(my_groceries)
# letter_to_check = input("What letter should we check?")

# counter = 0

# for item in grocery_list:
#     if item[0] == letter_to_check:
#         print(item)
#     else:
#         print("Nothing with that letter here")
#     counter += 1
#     print(counter)

# for i in range(len(grocery_list)): 
#     print(grocery_list[i])