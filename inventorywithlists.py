inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# count number of items in list
inventory_len = len(inventory)
# select first item, save it to variable
first = inventory[0]
# select last item, save it to variable
last = inventory[-1]
# select (splice) items index 2-5 (does not include 6), save to variable
inventory_2_6 = inventory[2:6]
# select (splice) first three items, save to variable
first_3 = inventory[:3]
# count how many "twin bed" instances there are, save to variable
twin_beds = inventory.count("twin bed")
#remove 5th element (index 4), save to variable
removed_item = inventory.pop(4)
# insert new item to list as 11th element (index 10)
inventory.insert(10, "19th Century Bed Frame")
# reverse sort inventory using .sort method
inventory.sort(reverse = True)
print(inventory)
# sort inventory using sorted() function, save to variable
sort_inventory = sorted(inventory)
print(sort_inventory)