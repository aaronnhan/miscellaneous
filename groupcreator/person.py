SQUARED_VAL_OFFSET = 2
NO_PICK_VAL = 10
class Person:
    def __init__(self, me, likes, dislikes):
        self.me = me
        self.likes = likes #hashmap person to rating
        self.dislikes = dislikes
    def get_hatred(self, person):
        if person.me in self.likes:
            #print(self.me + person.me + str(self.preferences.index(person.me)))
            return (self.likes.index(person.me) + SQUARED_VAL_OFFSET)**2
        if person.me in self.dislikes:
            return 3000
        return 100
    def swap(self, person):
        person.me, self.me = self.me, person.me
        person.likes, self.likes = self.likes, person.likes
        person.dislikes, self.dislikes = self.dislikes, person.dislikes
