# Organising sales data for a pizza place

#list for types of pizza we sell
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# list to track how much each kind of pizza slice costs
prices = [2, 6, 1, 3, 2, 7, 2]

# count occurances of 2$ slices, save to variable
num_two_dollar_slices = prices.count(2)

#find length of toppings list, save to variable
num_pizzas = len(toppings)

#print message
# print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

#make 2D toppings and prices list
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

#sort p&p in ascending price
pizza_and_prices.sort()

#select first element of sorted p&p list, save to variable
cheapest_pizza = pizza_and_prices[0]
#same, but last element
priciest_pizza = pizza_and_prices[-1]

# remove anchovies (last item in list)
pizza_and_prices.pop()

# add new pizza type, aligning it with the sorted prices list
pizza_and_prices.insert(4, [2.5, 'peppers'])

# select (slice) the three lowest cost pizzas and save to variable
three_cheapest = pizza_and_prices[:3]

print(pizza_and_prices)