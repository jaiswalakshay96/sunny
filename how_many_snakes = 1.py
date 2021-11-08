#scripting 1st problem



name = input("enter the name").split()
assignments = input("enter the assignment").split()
grades = input("enter the grades").split()

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
for name,assignments,grades, in zip(name,assignments,grades) :
    print(message.format(name,assignments,grades,int(grades) +10*int(assignments)))