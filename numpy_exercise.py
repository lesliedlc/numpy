import numpy as np

array_grades = np.random.randint(60,101,12).reshape(3,4) #array of 12 linear number between 60 and 101 with reshape to fit 3 rows of 4 columns
print(array_grades)

print("All grades:",array_grades.mean())
print("Each test:",array_grades.mean(axis = 0)) #avg grades for each test, per column
print("Each student:",array_grades.mean(axis = 1)) #avg grades per row, per student 

#axis = 0 is by columns & axis = 1 is by rows