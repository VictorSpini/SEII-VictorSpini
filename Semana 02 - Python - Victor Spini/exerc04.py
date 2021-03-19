# Working with Key-Value Pairs

student = {'name': 'John', 'age': 25, 'courses': ['Geografia', 'Literatura']}
print(student)
print(student['name'])
print(student['courses'])
# print(student[1])
print(student.get('phone', 'Not Found'))
student['phone'] = '55 9 9800 8546'
print(student.get('phone', 'Not Found'))
student['name'] = 'Victor'
print(student)
student.update({
    'name': 'Jane',
    'age': 26,
    'phone': '55 9 9854 9985',
    'courses': ['Geografia', 'Literatura']
})

age = student.pop('age')
print(student)
print(age)
student = {'name': 'John', 'age': 25, 'courses': ['Geografia', 'Literatura']}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)
