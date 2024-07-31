# a project to process data from a group of friends playing scrabble, using dictionaries.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# using dict comprehension and zip to create a dictionary, where the <letters> are the keys and the <points> are the values.
letters_to_points = {key:value for key, value in zip(letters, points)}
# adds an element to letters_to_points for the blank tile, with the key being an empty space and the value of 0.
letters_to_points[" "] = 0


# defines a function to take in a word and return how many points that word would be worth.
def score_word(word):
    point_total = 0
    # creates a loop to iterate through the letters in <word> and adds the point value of each letter to point_total
    for letter in word:
        # sets letter to uppercase, checks it against the letters_to_points dictionary, and adds its points to the point_total
        point_total += letters_to_points.get(letter.upper(), 0)
    return point_total


# creates a dictionary of the players and their words to be scored
player_to_words = {'player1':['BLUE', 'tennis', 'Exit'], 'wordNerd':['earth', 'eyes', 'machine'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['Zap', 'Coma', 'Period']}
player_to_points = {}


# iterates through each element in the player_to_words dict
for player, words in player_to_words.items():
    player_points = 0
    # iterates through each word in the player's lists
    for word in words:
        # adds the player's points by calling <score_word> and passing through the word argument
        player_points += score_word(word)
    player_to_points[player] = player_points

# defines a function that takes in a player and a word, and adds that word to the list of words that they've played
def play_word(player, word):
    player_words = player_to_words.get(player, 'Not playing')
    player_words.append(word)
    player_to_words[player] = player_words

# defines a function to turn the above nested loops into a function to call anytime.
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        # iterates through each word in the player's lists
        for word in words:
            # adds the player's points by calling <score_word> and passing through the word argument
            player_points += score_word(word)
        player_to_points[player] = player_points


# brownie_points = score_word("BROWNIE")
# print(letters_to_points)
# print(player_to_points)
print(player_to_words)
print(player_to_points)
play_word('Lexi Con', "platypus")
update_point_totals()
print(player_to_words)
print(player_to_points)