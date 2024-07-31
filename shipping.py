# This program will take the weight of a package and determine the cheapest way to ship it


weight = float(input('How much does this package weigh?'))
# weight variable is declared within a <float(input())> function to allow user input as a float.

if weight <= 0:  # disallowing the weight to be 0 or negative
    print('Error: invalid weight. Please enter a valid number.')

else:
    weight = round(weight, 2)
    print("For a package weighing " + str(weight) + ' pounds:')

    # shipping calculations, they don't need to run for an invalid weight. Starting with ground shipping:
    if weight <= 2:
        ground_ship_cost = weight * 1.50 + 20
    elif weight <= 6:
        ground_ship_cost = weight * 3 + 20
    elif weight <= 10:
        ground_ship_cost = weight * 4 + 20
    else:
        ground_ship_cost = weight * 4.75 + 20
    ground_ship_cost = round(ground_ship_cost, 2)
    print("Ground Shipping costs $" + str(ground_ship_cost))

    # premium shipping
    premium_ground_ship_cost = 125.00
    print("Premium Ground Shipping costs $" + str(premium_ground_ship_cost))

    # drone shipping
    if weight <= .5:
        drone_ship_cost = 2
    elif weight <= 2:
        drone_ship_cost = weight * 4.50
    elif weight <= 6:
        drone_ship_cost = weight * 9
    elif weight <= 10:
        drone_ship_cost = weight * 12
    else:
        drone_ship_cost = weight * 14.25
    drone_ship_cost = round(drone_ship_cost, 2)
    print("Drone Shipping costs $" + str(drone_ship_cost))

    # shipping method recommendation statements
    if premium_ground_ship_cost <= drone_ship_cost and premium_ground_ship_cost <= ground_ship_cost:
        print("We recommend Premium Ground Shipping at: $" + str(premium_ground_ship_cost))
    elif drone_ship_cost <= ground_ship_cost and drone_ship_cost <= premium_ground_ship_cost:
        print("We recommend Drone Shipping at: $" + str(drone_ship_cost))
    elif ground_ship_cost <= drone_ship_cost and ground_ship_cost <= premium_ground_ship_cost:
        print("We recommend Ground Shipping at: $" + str(ground_ship_cost))

# examples:
# 4.8lb = GS at $34.40
# 1.5lb = DS at $6.75
# 41.5lb = PGS at $125.00
