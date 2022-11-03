from casting.actor import Actor
from shared.point import Point
import random 

class Rock(Actor):
    '''A collection of rocks will fall from the top of screen down to the bottom for the actor to avoid.
    Catching a rock subtracts a point from the users total points.  '''

    def __init__(self):
        '''Constructs a new rock.'''
        super().__init__()
        self._is_alive = True
        self._score = 0
        self.position = Point(random.randint(2, 500), 0)
        self.points = 1
        self.move = 0
        
    def display(self):
        '''Sets a rock to an O.'''
        list = ["O"]
        self._text = random.choice(list)
        return self._text
    
    def get_score(self):
        '''Gets the current score and returns it.'''
        if self._text == "O":
            self._score -= 1
        return self._score
    
        
    def set_score(self, score):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._score = score
        
    def set_movement(self):
        """Sets movement of gem across screen."""
        
        if self.move < 20: 
            self.move += 1
            
        else: 
            self.position.y += 1
            self.move = 0
    
    def collide(self):
        """Controls points based on collision."""
        
        if self._is_alive == False:
            if list[0]:
                self._score -= 1
        else: 
            pass
