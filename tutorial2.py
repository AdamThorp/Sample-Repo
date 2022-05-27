# Print Welcome message

greeting = "Hello"
name = "Michael"

# message = greeting + ", " + name + ". Welcome!"
# message = "{}, {}. Welcome!".format(greeting, name)
message = f"{greeting}, {name.upper()}. Welcome!".format(greeting, name)

print(message)

print()
