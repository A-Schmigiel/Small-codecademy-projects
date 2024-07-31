# making a tuple
my_info = ('Avian', 29, 'Telephony')
#accessing elements is like with a list:
print(my_info[0]) #prints Avian
print(my_info[-1]) #prints Telephony
#unpack the tuple
name, age, job = my_info
print(age)
#one element tuple syntax:
one_ele_tuple = (4,) # saves one_ele_tuple as a tuple
not_tuple = (4) # saves not_tuple as an int, rather than a tuple
print(type(one_ele_tuple)) # prints <class 'tuple'>
print(type(not_tuple)) # prints <class 'int'>

