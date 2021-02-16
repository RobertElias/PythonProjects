# Grade Sorter App...
print("Welcome to the Grade Sorter App.")

#Initialize list and get user input
grades = []
grade = str(input("\nWhat is your first grade (0-100): "))
grades.append(grade)
grade = str(input("What is your second grade (0-100): "))
grades.append(grade)
grade = str(input("What is your third grade (0-100): "))
grades.append(grade)
grade = str(input("What is your fourth grade (0-100): "))
grades.append(grade)

print("Your grades are: " + str(grades))

#Sort
grades.sort(reverse = True)
print("\nYour grades from highest to lowest are: " + str(grades))

# Remove lowest two grades

print("\nThe lowest two grades will now be dropped.")
removed_grade = grades.pop()
print("Removed grade: " +  str(removed_grade))
removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade))

#Print remaining grades
print("\nYour remaining grades are: " + str(grades))

print("Nice work! Your highest grade is " + str(grades[0]) + ".")
