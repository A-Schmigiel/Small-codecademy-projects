#making a small fictional gradebook, mostly just a good reference for some list methods

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#starting subjects:
subjects = ['physics', 'calculus','poetry', 'history']
# starting grades
grades = [98, 97, 85, 88]
#2D list
gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]
# add in CS and VA classes and grades
gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])
#increase VA grade by 5 points
gradebook[-1][-1] = 98
#remove poetry grade, change to pass/fail
gradebook[2].remove(85)
gradebook[2].append('Pass')
# combine current and last semester gradebook 2D lists
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)