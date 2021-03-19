# Working with textual Data

print("Hello World")

message = "Hello World"
print(message)

message = "Bobby\'s World"
print(message)

message = "Hello World"
print(len(message))
print(message[0])
print(message[0:5])
print(message[6:])
print(message.lower())
print(message.upper())
print(message.count("l"))
print(message.find("World"))
print(message.find("Qualquer frase"))
message.replace("World","Qualquer frase")
print(message)
greeting = "Hello"
name = "Victor"
message = greeting + ", "+ name + ". Welcome!"
print(message)
message = "{}, {}. Welcome!".format(greeting,name)
print(message)
message = f"{greeting}, {name}. Welcome!"
print(message)
message = f"{greeting}, {name.upper()}. Welcome!"
print(message)
#print(dir(name))
#print(help(str))
#print(help(str.lower))

