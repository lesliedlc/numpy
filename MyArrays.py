import numpy as np

integers = np.array([1,2,3])

#print(integers)
#print(type(integers))

integers = np.array([[1,2,3],[4,5,6]])

'''
print(integers.dtype) #indicates the type of info in array
print(integers.ndim) #indicates the dimensions in integers
print(integers.shape) #tells the rows and columns/number of dimensions
print(integers.size) #number of elements
print(integers.itemsize) #amount of spaces between info

for row in integers:
    print(row)
    print()

    for col in row:
        print(col, end=' ') #prints each integer in array with space on same line
    print()

for i in integers.flat:
    print(i, end = ' ') #for loop prints out every element of all arrays 
    #the end = ' ' puts them all on same line

print(np.zeros(5)) #creates an array of five 0's [0,0,0,0,0] as floats

print(np.ones(5)) #creates array of five 1's as floats

array1 = np.ones((2,4),dtype = int) #give variable and dimension with the type 
print(array1)

array2 = np.full((3,5),13) #create array with 3 rows and 5 columns with the number 13 [[13,13,13,13,13],[],[]]
print(array2)

print(np.arange(5)) #creates array 0-4 with 5 as cap
print(np.arange(5,10)) #creates array 5-9
print(np.arange(10,1,-2)) #creates step value of going down by 2's from 10 with 1 as least value
print(np.linspace(0.0,1.0, num=5)) #will produce 5 numbers that are equally spaced with a max and min

array1 = np.arange(1,21) #creates array from 1-20
print(array1)

array2 = array1.reshape(4,5) #with array 1 info, it creates 4 rows with 5 columns each
print(array2) #needs to be same dimensions of what you want to reshape


array3 = np.arange(1,100001).reshape(4,25000)
print(array3)

array4 = np.arange(1,100001).reshape(100,1000)
print(array4)
'''

numbers = np.arange(1,6)

print(numbers * 2) #multiplies every number by 2 but doesnt modify original array
print(numbers) #original array not modified

numbers += 10 #augmented assingments modify original array ex:original = 1 , now = 11, etc
print(numbers)

print(numbers  ** 3) #exponent of the array that was modified bc aug. assign permanately modify them but doing it in print DOESNOT perm. modify

print(numbers >= 13) #tells you what numbers are greater than 13 from the array 

numbers2 = np.arange(5,10)

print(numbers2 > numbers) #compares two arrays - true or false
print(numbers == numbers2)

