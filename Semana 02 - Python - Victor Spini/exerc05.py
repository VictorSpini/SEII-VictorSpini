# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# and
# or
# not

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.


language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'JavaScript':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad Creds')


user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:
    print('Admin page')
else:
    print('Bad Creds')

user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log in')
else:
    print('Welcome')


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(id(a))
print(id(b))
print(a is b)
b = a
print(id(a))
print(id(b))
print(a is b)


condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

