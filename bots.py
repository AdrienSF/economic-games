from sprites import AgentSprite
from psychopy import visual, event, core
import random


class BaseBot():
    def __init__(self, win, name, pos=(0,0), money=0):
        self.window = win
        self.name = name
        self.pos = pos
        self.money = money

        self.sprite = AgentSprite(win, name)

        self.wait_stim = visual.TextStim(win, text='waiting for ' + name + ' to move...', units='norm')

        self.update()

    def update(self):
        self.sprite.pos = self.pos
        self.sprite.credit_stim.text = str(self.money)


    def draw(self):
        self.update()
        self.sprite.draw()



class InvestmentBot(BaseBot):
    def __init__(self, win, name, pos=(0,0), money=0):
        BaseBot.__init__(self, win, name, pos, money)
        self.sprite.disp_credits = True


    def get_move(self):
        # display waiting for [name] to move for random amount of time to pretend it's human
        self.wait_stim.draw()
        self.window.flip()
        core.wait(random.choice(range(10)))

        move = random.choice(range(self.money+1))
        self.money -= move

        return move


