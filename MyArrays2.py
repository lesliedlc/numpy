import numpy as np 
'''
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.std()) #standard deviation
print(grades.var()) #variant

print(grades.mean(axis=0))#axis=0 will calculate means of each columns across arrays

print(grades.mean(axis = 1)) #give avg of every/each array 

numbers = np.array([1,4,9,16,25,36])

print(np.sqrt(numbers))

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

print(grades[0,1]) #0 is the first row and 1 is the 2nd column bc 0 would be first column
print(grades[1]) #gives complete row

print(grades[0:2]) #will give first 2 columns (0 and 1st column) - splice
print(grades[[1,3]]) #with the double brackets it will give the entire rows of 1 and 3 as requested

print(grades[:,0]) #gives us the first column of every row

print(grades[:,1:3]) #all the rows, with columns 1-3 

#NUMPY = NUMERICAL PYTHON
'''

#shallow copies
numbers = np.arange(1,6)
numbers2 = numbers.view() #shallow view to the array not a copy, since any change here will affect the original array
#print(numbers2)
numbers[1] *= 10
#print(numbers2)
numbers2[1] /= 10
#print(numbers)

#list slicing
numbers2 = numbers[0:3]
#print(numbers2)
numbers[1] *= 20
#print(numbers2)

#deepcopy
numbers2 = numbers.copy()

grades = np.array([[87,96,70],[100,87,90]])
#print(grades.reshape(1,6)) #creates a copy that will affect the original, shallow/view
#print(grades)

flattened = grades.flatten() # flatten puts it all into one line
#print(flattened)
#print(grades)

raveled = grades.ravel() #same as flatten
#print(raveled)
raveled[5] = 99 #might get an error if out of bounds in ravel index
#print(grades)

grades2 = grades.T #transposed, columns combine to rows, switch them
#print(grades2)
#print(grades)

grades = np.array([[87,96,70],[100,87,90]])
grades2 = np.array([[94, 77, 90],[100,81,82]])

h_grades = np.hstack((grades,grades2)) #hstack = horitzonal, add more grades to students
print(h_grades)

v_grades = np.vstack((grades,grades2))
print(v_grades)
#vstack add more students, vertical, added 2 more rows



