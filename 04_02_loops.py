for x in range(6):
    print(x)

# 0,1,2,3,4,5

my_list = [1, 2, 3, 4]
for value in my_list:
    print(value)

# 1,2,3,4

languages = [
    "Java",
    "Javascript",
    "Python",
    "Rust",
    "Go"
]
new_list = []

for language in languages:
    if "J" in language:
        new_list.append(f'{language} 🍄')

print(new_list)
# ['Java 🍄', 'Javascript 🍄']


my_dict = {
    'color': 'blue',
    'fruit': 'apple',
    'pet': 'dog'
}

for key in my_dict:
    print(f"{key} -> {my_dict[key]}")

# color -> blue
# fruit -> apple
# pet -> dog
