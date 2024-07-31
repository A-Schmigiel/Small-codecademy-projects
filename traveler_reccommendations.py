# program to recommend venues, restaurants, historical sites to user, based on their interests
# (part of git/python practice)
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
# traveler info list
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
# attractions list initialisation. List containing empty lists for each location in the above destinations list.
# to be filled later.
attractions = [[]for place in destinations]


# function to retrieve the index of a destination from within the <destinations> list, using a passed in <destination> parameter value
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


# function to use the test_traveler info list and get_destination_index to retrieve the index of the desired destination,
# using a passed in <traveler> value
def get_traveler_location(traveler):
    # location is the second element (index 1) in the traveler list; sets as traveler_destination
    traveler_destination = traveler[1]
    # sets traveler_destination_index using the get_destination_index function and the traveler_destination variable
    # we just made
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


# function to add an attraction to <attractions> list, using passed in <destination> and <attraction> parameter values
def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    # uses the destination_index to save the appropriate <attractions> sublist to attractions_for_destination variable
    attractions_for_destination = attractions[destination_index]
    # appends the new <attraction> (entered while calling add_attraction) to the attractions_for_destination list
    attractions_for_destination.append(attraction)
    return attractions_for_destination


# function to search through the <destination> city's attractions and cross-reference attraction tags and the passed
# through <interests> list parameter, to return a list of potentially interesting attractions for our traveler
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    # pulls the <destination> city's attractions sublist, saves to attractions_in_city
    attractions_in_city = attractions[destination_index]
    # initialising empty list of attractions with the passed through <interest>
    attractions_with_interest = []
    # loops through each element in the above attractions_in_city list
    for possible_attraction in attractions_in_city:
        # saves the tagged interests (element at index 1 in each <attraction>'s sublist)
        attraction_tags = possible_attraction[1]
        # loops through each <interest> in the passed-through list (during the find_attractions function call)
        for interest in interests:
            # checks if the element in the <interests> list is also in the <attraction>'s tags
            if interest in attraction_tags:
                # adds the attraction with the confirmed interest to the attractions_with_interest list,
                # using .append on the city's possible_attractions list, calling the element at index 0,
                # to return the attraction's name
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest


# function to connect the traveler with the attractions that fit their interests
def get_attractions_for_traveler(traveler):
    # saves the traveler's destination using the second element (index 1) in their information list
    traveler_destination = traveler[1]
    # same as above, using their interest list at index 2 in their list
    traveler_interests = traveler[2]
    # passes the traveler_interests and traveler_destination variables into the function call parameters for
    # find_attractions, saving the resulting attractions list to a variable
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    # string to show traveler, using the first element in the traveler's info list (their name) and a greeting
    interests_string = "Hi, " + str(traveler[0]) + "! "
    # conditional if/elif statement to fix legibility in interests_string for low results, and update
    # interests_string appropriately
    if len(traveler_attractions) < 1:
        interests_string = interests_string + traveler_destination + " is full of adventure waiting for you! We think you'll love exploring the city"
    elif len(traveler_attractions) == 1:
        interests_string = interests_string + "We think you'll like this attraction around " + traveler_destination + ": " + traveler_attractions[0]
    elif len(traveler_attractions) > 1:
        interests_string = interests_string + "We think you'll like these places around " + traveler_destination + ": "
        # loops through traveler_attractions list (excluding last element) to add them to the interests_string, plus comma and space for readability
        for index in range(len(traveler_attractions)- 1):
            interests_string = interests_string + traveler_attractions[index] + ", "
        # last element, ending without the comma/space
        interests_string = interests_string + "and " + str(traveler_attractions[-1])

    return interests_string + ". Enjoy your visit!"


# adding attractions to <attractions> sublists via add_attractions function
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# sample travelers
smith_dereck = ['Dereck Smith', 'Paris, France', ['monument']]
mcpherson_melanie = ['Melanie McPherson', 'Cairo, Egypt', ['zombies']]
guy_johnny = ['Johnny Guy', 'Shanghai, China', ['museum', 'garden', 'skyscraper']]

# test for single attraction return, using [name, destination, and [interests]], saves to variable
print(get_attractions_for_traveler(smith_dereck))
# test for null return
print(get_attractions_for_traveler(mcpherson_melanie))
# test for multiple returns
print(get_attractions_for_traveler(guy_johnny))