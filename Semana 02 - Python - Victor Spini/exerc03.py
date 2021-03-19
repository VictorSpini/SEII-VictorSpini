# Lists, Tuples and Set

courses = ['Física', 'Literatura', 'Geografia', 'Informatica']

print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:2])
print(courses[1:])

courses.append("Artes")
print(courses)

courses.insert(0, "Psicologia")
print(courses)

courses_2 = ["Matematica", "Portugues"]
courses_1 = []
courses_1.extend(courses)
courses_1.insert(0, courses_2)
print(courses_1)
courses.extend(courses_2)
print(courses)

courses.remove("Portugues")
print(courses)

popped = courses.pop()
print(courses)
print(popped)

courses.reverse()
print(courses)

courses.sort()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
nums.sort()
print(courses)
print(nums)
nums.sort(reverse=True)
sorted_courses = sorted(courses)
print(nums)
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index("Informatica"))

print("Artes" in courses)

for index, course in enumerate(courses, stArtes=0):
    print(index, course)

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)

# Mutable
list_1 = ['Geografia', 'Física', 'Literatura', 'Informatica']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Artes'

print(list_1)
print(list_2)


# Immutable
tuple_1 = ('Geografia', 'Física', 'Literatura', 'Informatica')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Artes'

print(tuple_1)
print(tuple_2)

# Sets
cs_courses = {'Geografia', 'Física', 'Literatura', 'Informatica'}
Artes_courses = {'Física', 'Artes', 'Design', 'Geografia'}
print(cs_courses)
print(Artes_courses)
print(cs_courses.intersection(Artes_courses))
print(cs_courses.difference(Artes_courses))
print(cs_courses.union(Artes_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}  # This isn't right! It's a dict
empty_set = set()
