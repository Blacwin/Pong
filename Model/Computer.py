

class Computer:
    def __init__(self, ob1, ob2, ob3):
        self.ob1 = ob1
        self.ob2 = ob2
        self.ob3 = ob3

    def logic(self, ob, level="easy"):
        ball = self.ob3.rect.y
        obj = ob.rect.y
        if level == "easy":
            if ball > obj + 50:
                ob.UP = False
                ob.DOWN = True
                ob.move()
            elif ball < obj + 50:
                ob.DOWN = False
                ob.UP = True
                ob.move()

    def play_to_player(self):
        self.ob2.UP, self.ob2.DOWN = False, False
        if self.ob3.rect.x > 400:
            self.logic(self.ob2)

    def play_to_yourself(self):
        self.ob1.UP, self.ob1.DOWN = False, False
        self.ob2.UP, self.ob2.DOWN = False, False
        if self.ob3.rect.x > 400:
            self.logic(self.ob2)
        elif self.ob3.rect.x < 400:
            self.logic(self.ob1)
