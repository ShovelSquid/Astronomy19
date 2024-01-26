class Person():
    def __init__(self, name, age, pronouns):
        self.name = str(name)
        self.age = str(age)
        self.pronouns = str(pronouns)
        self.species = "human"
        self.heart = "normal"

        # Opinions:
        self.favorites = {
            'movie': {
                'name': '',
                'opinion': '',
                'year_made': 0,
                'times_seen': 0
            },
            'food': {
                'name': '',
                'opinion': '',
                'country': '',
                'can_make': False
            }
        }
    def printFavorites(self):
        # make sure we actually have favorite things (hopefully not, I want to be special)
        for key in self.favorites.keys():
            if (self.favorites[key]['name'] != ''):
                self.printFavorite(key)

    
    def printFavorite(self, key): 
        # make sure we actually have a favorite whatever
        # key is the type of favorite thing we have, like a movie, food, whatever
        # check if we have data about that thing:
        if (self.favorites[key]['name']) != '' or None:         # if it doesn't exist or if it is default
            fav = self.favorites[key]       # save dictionary 'filepath' for easy access
            print("My favorite " + key + " is " + fav['name'] + ".")        # print name of favorite thing

            # check if we have an opinion about that thing
            if ('opinion' in fav):          # 1st if it exists in dict
                if (fav['opinion'] != '' or None):          # 2nd if its not empty
                    print("I think that " + fav['opinion'])         # print the opinion

            # check for year made
            if ('year_made' in fav):        # same deal; check if it exists
                if (fav['year_made'] != 0 or None):         # then check if its empty, like my skull
                    print(fav['name'] + " was made in " + str(fav['year_made']))        # printer action
                #   (", and I've seen it 12 times since then.") if fav['times_seen'] != '' or None else ".")       # this if/else checks in the same line if we've seen the movie before
            
            # check for times seen
            if ('times_seen' in fav):
                if (fav['times_seen'] != 0 or None):
                    print("I've seen " + fav['name'] + " " + fav['times_seen'] + " times since it came out.")

            # check favorite country
            if ('country' in fav):
                if fav['country'] != '' or None:
                    print(fav['name'] + " comes from " + fav['country'] + ".") 

            # check if makeable
            if ('can_make' in fav): 
                can = " indeed"         # expression for makeable
                if fav['can_make'] == False:
                    can = "not, in fact,"          # expression for not makeable
                print("I can" + can + " make " + fav['name'])
    
    
    def presentSelf(self):
        print(self.name + " is a " + self.age + " year old " + self.species 
            + " with a big heart." if self.heart != "normal" else " who lives life.")
        print(self.name + " goes by " + self.pronouns + " pronouns.")
        self.printFavorites()



# initializing Kaelen as a human being
Kaelen = Person("Kaelen Cook", 21, "he/him")
Kaelen.heart = "big"
Kaelen.species = "frog descendent (aka french)"
# infographics about Kaelen's favorite movie
favmovie = Kaelen.favorites['movie']
favmovie['name'] = "Edge of Tomorrow"
favmovie['opinion'] = """Edge of Tomorrow is an absolutely fantastic movie; not only does it tick all of my aesthetic boxes 
(crazy cool tentacle-y alien invasions, time loop groundhog day shenanigans, MECHS, TOM CRUISE?!!! BADASS ANGEL EMILY BLUNTT?!?!!?!), 
there is also a lot more depth than meets the eye to this film. Not only is it an action war movie, 
it's also a romance movie, a spy thriller, an end of war film, and so much much more; 
This movie is everything and everyone that ever was and ever will be, I love it so much."""

favmovie['year_made'] = 2014
favmovie['times_seen'] = "too many"
# infographics about Kaelen's favorite food
favfood = Kaelen.favorites["food"]
favfood['name'] = "sushi"
favfood['opinion'] = """sushi is delicious; expertly crafted and an example of sophistication and deliciousness from simplicity; 
also a vision of a brighter agricultural future with using fish and rice and sustaining the world and possibly astronauts in space 
with aquaponics in tasty and nutritious ways."""
favfood['country'] = "Japan"
favfood['can_make'] = False


# showtime, baby
Kaelen.presentSelf()