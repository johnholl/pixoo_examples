import math

FONT_HEIGHT=6

class MoveableText:
    def __init__(self, text, initial_x, initial_y, can_move, screen, color=(255, 255, 255)):
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.x = initial_x
        self.y = initial_y
        self.text = text
        self.can_move = can_move
        self.screen = screen
        self.screen.draw_text(self.text, (self.x, self.y), color)
        self.color = color
    
    def reset(self):
        self.screen.draw_filled_rectangle((min(self.x, 63), min(self.y, 63)),
                                                (min(self.x + 4*len(self.text), 63), min(self.y + FONT_HEIGHT, 63)), (0, 0, 0))
        self.x = self.initial_x
        self.y = self.initial_y
        self.screen.draw_text(self.text, (self.x, self.y), self.color)

    def move(self, del_x, del_y):
        if not self.can_move:
            return
        
        # clear horizontal strip
        self.screen.draw_filled_rectangle((min(self.x, 63), min(self.y, 63)),
                                          (min(self.x + 4*len(self.text), 63), min(self.y + FONT_HEIGHT, 63)), (0, 0, 0))

        #
        self.x = self.x + 4*del_x
        self.y = self.y + 5*del_y
        if self.x + 4*len(self.text) < 0 or self.x > 59 or self.y > 58 or self.y < 0:
            return
        
        start_index = 0
        if self.x < 0:
            start_index = math.ceil(-1.0*self.x/4)
        
        end_index = len(self.text)
        end_index = end_index - max(math.ceil((self.x + len(self.text)*4 - 63)/4.0), 0)
        
        print(start_index)
        print(end_index)
        print(self.x, ", ", self.y)
        self.screen.draw_text(self.text[start_index:end_index], (max(self.x,0), max(self.y,0)), self.color)
        print(self.x, ", ", self.y)