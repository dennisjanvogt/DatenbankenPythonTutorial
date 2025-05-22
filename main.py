from container import Student


studenten = Student.get_all()

for stu in studenten:
    print(dir(stu))
