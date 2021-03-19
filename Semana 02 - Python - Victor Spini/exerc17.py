# Variable Scope - Understanding the LEGB rule and global/nonlocal statements

LEGB
Local, Enclosing, Global, Built-in

# import builtins

# print(dir(builtins))

# def my_min():
#   pass

# m = min([3, 7, 8, 11, 13])
# print(m)

# x = 'global x'

# def test(z):
#   global x
#   y = 'local y'
#   x = 'local x'
#   print(y)
#   print(x)
#   print(z)

# test('local z')
# print(y)
# print(x)
# print(z)

for a in range(2):
    x = 'global {}'.format(a)


def outer():
    # x = 'outer x'
    for b in range(3):
        x = 'outer {}'.format(b)

    def inner():
        # nonlocal x
        # x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c)
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)


outer()
print(x)
print(a)

# End
