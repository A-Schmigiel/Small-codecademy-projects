import random

# variables for fun
# name = 'Stephan Vanderbilt McJones III'
# question = 'Will the farmhand fuck me in the new Carriage?'
name = str(input('What is your name?'))
question = str(input('What is your question?'))
answer = ''
random_number = random.randint(1, 13)

# This if/elif/else chain uses random_number to select an answer
if random_number == 1:
    answer = 'Yes - definitely'
elif random_number == 2:
    answer = 'It is decidedly so'
elif random_number == 3:
    answer = 'Without a doubt'
elif random_number == 4:
    answer = 'Reply hazy, try again'
elif random_number == 5:
    answer = 'Ask again later'
elif random_number == 6:
    answer = 'Better not tell you now'
elif random_number == 7:
    answer = 'My sources say no'
elif random_number == 8:
    answer = 'Outlook not so good'
elif random_number == 9:
    answer = 'Very doubtful'
elif random_number == 10:
    answer = 'It has been foretold'
elif random_number == 11:
    answer = 'You betcha, sweetie'
elif random_number == 12:
    answer = 'You should make this decision, not me'
elif random_number == 13:
    answer = 'This will be your DOOM'
else:
    answer = 'Error'

if name == '' and question == '':
    print('I cannot answer that which the nameless one does not ask.')
elif name == '':
    print('A nameless one asks: ' + question)
elif question == '':
    print('Ask your question, young ' + name + ', and receive my wisdom.')
else:
    print(name + ' has asked: ' + question)

if question != '':
    print('The magic ball responds with: ' + answer + '.')
