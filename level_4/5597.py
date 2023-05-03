count = 0
course = [x for x in range(1,31)]
while count < 28:
    student = int(input())
    course.remove(student)
    count += 1
print(min(course))
print(max(course))