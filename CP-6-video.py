#dictionaries can let you create keys or variables inside a list which you can address
#directly from your code isntead of running a list
my_dict = {
    'key': 'value',
    1: 'spaghetti',
    2: 'pasta',
    3: 'pizza',
    'cats': 'No Thanks',
    10.5: 4
    }

my_dict['new key'] = 'Alphonse'
my_dict[2] = 'cheesy bread'
my_dict[2] = 'endless breadsticks'
# del my_dict[2]

# print(my_dict)

# x = my_dict[3]
# print(x)

#use this for looping on your dictionary, since there are 2 things in a dictionary
for key, value in my_dict.items():
    print(f'The key is {key}')
    print(f'And this is the value: {value}')

#gives you back the keys
for key in my_dict.keys():
    print(key)

#Will give you back all the velues
for value in my_dict.values():
    print(value)
# ALSOOO!!! K STANDS FOR K AND V STANDS FOR VALUE IN REGULAR CODE

my_dict = {
    'soccer': ['Manchester City', 'Bayern Munich', 'Seattle Sounders'],
    'formula one': {'driver' : 'checo'},
    'football': {'nfl': ['seahawks', 'packers', 'NOT THE PATS'],
                 'college': ['Cleamson', 'UCLA', 'ANYONE BUT ALABAMA']}
}

print(my_dict['soccer'][1])

#For a list you need an index, for dic you need a key name
print(isinstance('Hello MF', str))



