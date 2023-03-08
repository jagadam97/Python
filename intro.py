message = "Jagadam's World"
print(message)
print('Hello World')
print(message[3])
print(message[0:7])  # first is inclusive but last is not
print(len(message))

print(message.lower())
print(message.upper())
print(message.count('a'))
print(message.find('World'))
new_message = message.replace('Jagadam','Dinesh')
print(new_message)

greeting = 'Hello'
name = 'Dinesh'
message = '{}, {}. Welcome!'.format(greeting,name)
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

print(dir(name))
print(help(str))
