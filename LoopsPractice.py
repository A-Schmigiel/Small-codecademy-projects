hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# set total price variable, loop through prices to add together
total_price = 0
for price in prices:
    total_price += price

# find average price, print (need to change int <average_price> value to str)
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(round(average_price, 2)))

# reduce each price by 5
new_prices = [price-5 for price in prices]
print(new_prices)

# Check incoming revenue
total_revenue = 0
# use a <for> loop to add the product of prices[i] (price at index i) and last_week[i]
# (how many customers got that haircut last week) to total_revenue at each step
for i in range(len(hairstyles)):
    total_revenue += (prices[i] * last_week[i])
print("Total revenue: " + str(total_revenue))

# find average daily revenue
average_daily_revenue = total_revenue / 7
print("Average daily revenue: " + str(average_daily_revenue))

# list comprehension to make list of haircuts under 30. Uses range to make sure it loops for the number of indexes in
# <new_prices>, checks the price to see if it is under 30, and if so, adds the corresponding hairstyle to the list.

# i = index. the below is an example of the syntax involved. It makes a new list of every entry in old_list,
# for which the entry at i of different_list is < 0:

# new_list = [old_list[i] for i in range(len(old_list)) if
# different_list[i] < 0]
cuts_under_30 = [hairstyles[i] for i in (range(len(new_prices))) if new_prices[i] < 30]
print(cuts_under_30)
