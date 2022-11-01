from casting.actor import Actor
import random 

class Gem(Actor):
    '''A collection of gems will fall from the top of screen down to the bottom for the actor to catch.
    Catching a gem adds a point to the users total points.  '''

    def __init__(self):
        '''Constructs a new gem.'''
        super().__init__()
        self._is_alive = True
        self._score = 0
        
    def display(self):
        '''Sets a gem to an *.'''
        list = ["*"]
        self._text = random.choice(list)
        return self._text
    
    def get_score(self):
        '''Gets the current score and returns it.'''
        if self._text == "*":
            self._score += 1
        return self._score
    
        
    def set_score(self, score):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._score = score
    
    def collide(self):
        if self._is_alive == False:
            if list[0]:
                self._score -= 1
        elif self._is_alive == False:
            if list[1]:
                self._score += 1
        else: 
            pass