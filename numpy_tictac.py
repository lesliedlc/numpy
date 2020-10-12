import numpy as np
import random
#1 [[,,],[,,],[,,]]
#2 let user choose row, col num to put X
#3 computer chooses random int 0-2 , if its already occpied, go to while board
# output: [[O,,X],[X,X,],[O,O,]] --array
#5 ex: 
'''
array = np.array([[X,O,O],[X,O,X],[O,X,O]])
count_row = np.count_nonzero(myarray == 'X') ##count all x in the whole array
count_row = np.count_nonzero(myarray == 'X', axis = 1) #count x per row
count_column = np.count_nonzero(myarray == 'X', axis = 0) #count x per column

# for the last two, rows and columns, if any element in array = 3, then user wins, then repeat = false
# while board[r,c] == 'x' or ''o', get row column again, until it finds a non occupied spot

#put it on board
# print board
# get row count, column count for computer
#if any element = 3, then comp wins, repeat = false
'''

