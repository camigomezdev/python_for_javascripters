n_cats = 10

if n_cats < 3:
    print("So sad")
elif n_cats >= 3 and n_cats <= 5:
    print("Nice!")
else:
    print("You are a lucky person!")

# You are a lucky person!

n_cats = 3
message = "Nice!" if n_cats >= 3 else "So sad"

print(message)
# Nice!