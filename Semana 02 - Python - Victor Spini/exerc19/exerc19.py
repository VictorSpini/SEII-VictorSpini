# Using Try/Except Blocks for Error Handling

try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close
finally:
    print('Executing Finally...')

try:
    f = open('curruptfile.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except IOError as e:
    print(f'First!\n {e}')
except Exception as e:
    print(f'Second!\n {e}')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')

# End
