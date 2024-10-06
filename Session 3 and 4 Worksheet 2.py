# List
courses = ['Introduction to Programming','Calculus I','Data Structures and Algorithms', 'Linear Algebra','Physics I','Chemistry I','Biology I','Microeconomics','Psychology I','History I','English Composition I','Introduction to Philosophy','Calculus II','Discrete Mathematics']
print(courses)
#  2.1: Sorting the list alphabetically without modifying the original list
sorted_courses = sorted(courses)
print( sorted_courses)
#  2.3: Sorting the list in reverse alphabetical order
reverse_sorted_courses = sorted(courses, reverse=True)
print( reverse_sorted_courses)
#  3.1: Reverseing the order of the original list
courses.reverse()
print( courses)
#  3.3: Reverseing the order again
courses.reverse()
print("Re-reversed list of courses:", courses)
#  4.1: Permanently sorting the list in alphabetical order
courses.sort()
print("Permanently sorted list of courses:", courses)
# 4.3: Sorting the list in reverse alphabetical order permanently
courses.sort(reverse=True)
print("Permanently reverse sorted list of courses:", courses)

# Createing a sorted version of the original list
sorted_courses = sorted(courses)
print("The following courses are available for expression of interest if the students meet the prerequisites:")

# 1.2. Printing the sorted available courses
for course in sorted_courses:
    print(course)

# 2.1: Replace a course 

original_course = 'Calculus II'
new_course = 'ICT 101'
index = courses.index(original_course)
courses[index] = new_course
print(f"The course '{original_course}' has been withdrawn and replaced by '{new_course}'.")

# adding new course
# 3.2. Using insert() to add a new course at the beginning of the list
courses.insert(0, "Artificial Intelligence") 

# 3.3. Using insert() to add a new course to the middle of the list
courses.insert(len(courses) // 2, "Machine Learning")  

# 3.4. Using append() to add a new course to the end of the list
courses.append("Web Development")  

print("Updated list of available courses:")
for course in courses:
    print(course)

  


# List to store unavailable courses
unavailable_courses = []

# Removeing four courses from the available list
for _ in range(4):
    # Removeing the first course in the list and add it to unavailable_courses
    removed_course = courses.pop(0)  # Removes the first course
    unavailable_courses.append(removed_course)  # Store the removed course


print("Due to technical and room availability issues, the following courses are unavailable:")
for course in unavailable_courses:
    print(course) 

print("\nRemaining available courses:")
for course in courses:
    print(course)  


#Tuleps and loops

# Createing a list of tuples (course_id, course_name)
courses = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
]

# 1.2: Createing an empty list to store course names
course_names = []

# : Looping through each tuple in the list
for course in courses:
    #  2.1: Extracting the course ID and name from the tuple
    course_id, course_name = course  

    #  2.2: Adding the course name to the empty list
    course_names.append(course_name)

print("The following courses are available:")
for name in course_names:
    print(name)  
