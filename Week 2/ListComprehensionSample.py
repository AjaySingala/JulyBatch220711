names = ["john", "Batman", "Neo"]
new_names = []

for n in names:
    if n.islower():
        n = n.capitalize()
    else:
        n = "Relax " + n.capitalize()

    new_names.append(n)

print(new_names)
names = new_names
print(names)

# List comprehension.
print("\nUsing List Comprehension...")
names = ["john", "Batman", "Neo"]
print("Before: ", names)
names = [n.capitalize() if n.islower() else "Relax " + n.capitalize() for n in names]
print("After: ", names)

# Hidden message.
print("\nUsing List Comprehension for multiple if-else statements...")
msg = "hi442nm233ag2"   # "hiddenmessage"
new_msg = "".join(
    ["d" if i == "4"
        else "e" if i == "2"
        else "s" if i == "3"
        else i
        for i in msg
    ]
)
print(msg)
print(new_msg)


# Regular looping
print("\nRegular looping...")
names = ["john", "Batman", "Neo"]
for name in names:
    print(name)
print("\nRegular looping with List comprehension...")

[print(name) for name in names]
