# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:
# Function takes temp input in Fahrenheit and converts it to celsius
def f_to_c(f_temp):
    # F to C conversion formula
    c_temp = (f_temp - 32) * 5/9
    # return C to be used outside the function scope
    return c_temp


# test variable
f100_in_celsius = f_to_c(100)


# Convert Celsius temp to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp


# test variable
c0_in_fahrenheit = c_to_f(0)


# function to perform force calculations
def get_force(mass, acceleration):
    return mass * acceleration


# testing
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")


# function to perform energy calculations, setting c to default
def get_energy(mass, c=3*10**8):
    return mass * (c**2)


bomb_energy = get_energy(bomb_mass)


print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")


def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration) * distance
    return force


# testing
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
