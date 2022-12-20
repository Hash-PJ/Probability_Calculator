import copy
import random

class Hat:
    def __init__(self, **args):
        self.balls = args
        self.contents = []
        for k,v in self.balls.items():
            ls = [k for i in range(v)]
            self.contents.extend(ls)
        #print(self.contents)

    def draw(self, nBalls):
        if nBalls>len(self.contents):
            return self.contents
        drawnBalls = random.choices(self.contents, k=nBalls)
        for ball in drawnBalls:
            if ball in self.contents:
                self.contents.remove(ball)
        return drawnBalls
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    wins = 0
    for i in range(num_experiments):
        cexpected = copy.deepcopy(expected_balls)
        chat = copy.deepcopy(hat)
        colors_drawn = chat.draw(num_balls_drawn)
        elist = []
    
        for k, v in expected_balls.items():
            elist += v * [k]
        
        # print("belist = ", len(elist))
    
        for x in colors_drawn:
            if x in elist:
                elist.remove(x)
            else:
                pass
        # print("lelist = ", len(elist))
        if len(elist) < 1:
            wins += 1
    return wins/num_experiments
