# program to create a dog adoption simulator.
# class examples: Breed, Owner, Tricks
# Attribute (what it is) examples: size (if over x inches tall or over x lbs, S/M/L/XL), friendliness, vocal, coat texture, hypoallergenic,
# long/short haired, drool levels, healthy, clean
# Methods (verbs/what they can do): be pet by owner, be trained by trainer, drink, eat, drool, sit, lie down, roll over,
# have a birthday, bark, beg, walk, piddle, run away, become friends, be adopted, roll in mud

# further improvements: add Tricks class, more methods

class Dog:
    def __init__(self, name, breed, weight, color, fur_length, gender, owner = 'None', is_clean = True, is_healthy = True, is_friendly = True, age = 0):
        self.name = name.title()
        self.gender = gender.lower()
        self.breed = breed.title()
        self.weight = weight
        self.color = color.lower()
        self.fur_length = fur_length.lower()
        self.is_clean = is_clean
        self.is_healthy = is_healthy
        self.is_friendly = is_friendly
        self.age = age
        self.size = self.pup_size()
        self.maturity = self.pup_maturity()
        self.owner = owner.title()
        self.pronoun = self.pup_pronoun()
        self.clean = self.cleaned()

    def __repr__(self):
        description = '{name} is a {maturity} {breed}, with a {length}, {color} coat'.format(gender = self.gender, length = self.fur_length, name = self.name, size = self.size, breed = self.breed, color = self.color, maturity = self.maturity)
        if not self.is_healthy:
            description += ' and some health concerns.'
        if self.is_friendly:
            description += '. A friendly dog, {name} is eager to meet new people!'.format(name = self.name)
        else:
            description += ' A nervous dog, {name} needs a bit more socialization and patience.'.format(name = self.name)
        if self.owner != 'None':
            description += ' {pronoun} belongs to {owner}.'.format(pronoun = self.pronoun.title(), owner = self.owner)
        return description

    def pup_maturity(self):
        if self.age <= 1:
            self.maturity = 'puppy'
        elif self.age <= 10:
            self.maturity = 'adult'
        else:
            self.maturity = 'senior'
        return self.maturity

    def pup_size(self):
        if self.weight <= 20:
            self.size = 'tiny'
        elif self.weight <= 30:
            self.size = 'small'
        elif self.weight <= 50:
            self.size = 'medium'
        elif self.weight <= 90:
            self.size = 'large'
        else:
            self.size = 'giant'
        return self.size

    def cleaned(self):
        if self.is_clean:
            return '{name} is all clean!'.format(name = self.name)
        else:
            return '{name} needs a bath...'.format(name = self.name)

    def piddle(self):
        self.is_clean = False
        print('Oh no! ' + self.name + ' got too excited and piddled all over the floor!')
        print(self.cleaned())

    def pup_pronoun(self):
        if self.gender == 'male':
            self.pronoun = 'he'
        elif self.gender == 'female':
            self.pronoun = 'she'
        else:
            self.pronoun = 'they'
        return self.pronoun

    def meets_stranger(self):
        if self.is_friendly:
            if self.maturity == 'puppy':
                self.piddle()
            else: print(self.name + ' is so happy to meet you!')
        else:
            print(self.name + ' barked, wary of strangers.')

    def rolls_in_mud(self):
        self.is_clean = False
        print('Uh oh, {dog} found some mud to play in...'.format(dog = self.name))
        print(self.cleaned())

    def bathtime(self):
        print('Bathtime!!')
        self.is_clean = True
        if self.fur_length == 'long':
            print('Oh no! ' + self.name + ' shook, sending water droplets flying!')

class Owner:
    def __init__(self, name, gender, age, pets, is_nice = True):
        self.name = name.title()
        self.gender = gender.lower()
        self.age = age
        self.is_nice = is_nice
        self.pets = pets
        self.pronoun = self.owner_pronoun()
    def __repr__(self):
        description = '{name} is {age} years old'.format(name=self.name, age=self.age)
        if len(self.pets) < 1:
            description += ', and does not have any pets.'
        elif len(self.pets) == 1:
            description += ' and owns {pet}.'.format(pet = self.pets[0].title())
        elif len(self.pets) == 2:
            description += ' and is the owner of {pet1} and {pet2}.'.format(pet1 = str(self.pets[0]).title(), pet2 = str(self.pets[1]).title())
        else:
            if self.pronoun.lower() == 'they':
                description += '. {pronoun} own'.format(pronoun = self.pronoun.title())
            else:
                description += '. {pronoun} owns'.format(pronoun = self.pronoun.title())
            for pet in range(len(self.pets)-1):
                description += ' ' + self.pets[pet].title() + ','
            description += ' and ' + self.pets[-1].title() + '.'

        return description

    def owner_pronoun(self):
        if self.gender == 'female':
            self.pronoun = 'she'
        elif self.gender == 'male':
            self.pronoun = 'he'
        else:
            self.pronoun = 'they'
        return self.pronoun

    def adoption(self, dog):
        print("Let's introduce {owner} and {dog}.".format(owner = self.name, dog = dog.name))
        dog.meets_stranger()
        if dog.is_friendly and self.is_nice:
            self.pets.append(dog.name)
            dog.owner = self.name
            print('{name} and {dog} seem to be getting along well.'.format(name=self.name, dog=dog.name))
            print('Enjoy your new home with {name}, {dog} !'.format(name = self.name, dog = dog.name))
        elif self.is_nice:
            self.pets.append(dog.name)
            dog.owner = self.name
            print('{dog} is nervous, but seems to like {owner}.'.format(dog = dog.name, owner = self.name))
            print("Thanks to {name}'s patience, {dog} is relaxing.".format(dog= dog.name, name = self.name))
            print('Congrats {name}, {dog} has warmed up to you and is ready to go home!'.format(name = self.name, dog = dog.name))
        else:
            print("Hmmm...perhaps this isn't the best fit.")

    def give_bath(self, dog):
        if self.is_nice and dog.is_friendly:
            dog.bathtime()
            print('{dog} is clean now. Well done!'.format(dog = dog.name))


buck = Dog('BUCKY boy', 'Jack Russell terrier', 5, gender = 'male', fur_length='long', color = 'white', age = 0)
moogan = Dog('Moogan Freeman', 'Pitbull', 70, 'Black and White', 'short', gender = 'male', is_healthy= False, is_friendly = False, age= 13)
avian = Owner('Avian', 'Nonbinary', 29, ['steve', 'spOOk'])
joe = Owner('joe smiTH', 'male', 37, ['spot'])

print(avian)
print(joe)
print(buck)
print(moogan)
print()
joe.adoption(buck)
joe.give_bath(buck)
print()
avian.adoption(moogan)
moogan.rolls_in_mud()
avian.give_bath(moogan)
print()
print(avian)
print(joe)
print(buck)
print(moogan)
