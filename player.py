from sprites import AgentSprite
from psychopy import visual, event, core


class Player():
    def __init__(self, win, name, pos=(0,0), money=0):
        self.window = win
        self.name = name
        self.pos = pos
        self.money = money

        self.sprite = AgentSprite(win, name)

        self.update()

    def update(self):
        self.sprite.pos = self.pos
        self.sprite.credit_stim.text = str(self.money)


    def draw(self):
        self.update()
        self.sprite.draw()


class InvestmentPlayer(Player):
    def __init__(self, win, name, pos=(0,0), money=0):
        Player.__init__(self, win, name, pos, money)
        self.slider_message = "how much of your money would you like to 'invest'"
        self.sprite.disp_credits = True





    def get_move(self):
        # show slider from 0 to all money available to get move
        slider = visual.RatingScale(self.window, low=0, high=self.money, singleClick=True, scale=self.slider_message)

        while slider.noResponse:
            slider.draw()
            self.window.flip()
        move = slider.getRating()

        self.money -= move

        return move