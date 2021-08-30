from BIpy.session import Session
from player import Player
from sprites import AgentSprite
from psychopy import event, core, visual
import random

class BaseEngine(Session):
    def __init__(self, win, info, agents, rounds=4):

        blocks = [[self.run_lobby]] + [[self.run_round]*rounds]
        Session.__init__(self, info, blocks)

        self.window = win
        self.agents = agents


    def run_lobby(self, _=None):
        self.hide_trial()
        # do lobby things to pretend there are other human agents
        sprites = []
        player = None
        for i in range(len(self.agents)):
            # sprite = AgentSprite(win=self.window, name='P'+str(i))
            sprite = self.agents[i].sprite
            sprite.pos = (.9*(2*(i+.5)/len(self.agents)-1),0)
            if issubclass(type(self.agents[i]), Player):
                sprite.highlight = True
                player = i
            sprites.append(sprite)

        assert player != None


        message = visual.TextStim(self.window, text='Press enter to start', units='norm', pos=(0,-.6))

        wait_times = [random.choice(range(1,5)) for a in self.agents]
        wait_times[player] = None
        clock = core.Clock()
        while not all([sprite.disp_ready for sprite in sprites]):
            if 'return' in event.getKeys():
                sprites[player].disp_ready = True

            for i in range(len(wait_times)):
                if wait_times[i]:
                    if clock.getTime() > wait_times[i]:
                        sprites[i].disp_ready = True


            for sprite in sprites:
                sprite.draw()
            message.draw()
            self.window.flip()

        core.wait(1)
        for i in range(len(self.agents)):
            sprites[i].disp_ready = False


    def run_round(self, _=None):
        print('yes hello this is base engine')
        pass


class InvestmentGameEngine(BaseEngine): #does the bot start with money? does money reset each round or is everything carried over?
    def __init__(self, win, info, player, bot, initial_money=10, rounds=4):
        BaseEngine.__init__(self, win, info, [player,bot], rounds=rounds)
        self.player = player
        self.bot = bot
        self.initial_money = initial_money

        self.player.pos = (-.5,0)
        self.bot.pos = (.5,0)

        self.text_stim = visual.TextStim(self.window, text='', units='norm', pos=(0, -.5))

        self.left_arrow = visual.TextStim(self.window, text='<----------', units='norm', pos=(0,0))
        self.right_arrow = visual.TextStim(self.window, text='---------->', units='norm', pos=(0,0))

        self.amount_stim = visual.TextStim(self.window, text='', units='norm', pos=(0,-.1))



    
    def run_round(self, _=None):
        # allocate game budget (or round budget?)
        self.allocate_money()

        # draw situation, press enter to start turn?
        self.draw(message='you start with ' + str(self.player.money) + ' credits. press enter to continue')
        self.window.flip()
        event.waitKeys()
        
        # get move
        move = self.player.get_move()
        self.log({'player_move': move})

        # add money to the bot
        self.bot.money += 3*move

        # draw situation, press enter to continue
        self.draw_transfer(to_bot=True, amount=move, message='press enter to continue')
        self.window.flip()
        event.waitKeys()

        # get bot move
        move = self.bot.get_move()
        self.log({'bot_move': move})

        # add money to the player
        self.player.money += move

        # draw situation, press enter to continue
        self.draw_transfer(to_bot=False, amount=move, message='')
        self.window.flip()
        core.wait(2)

        self.log({'player money at end of trial': self.player.money, 'bot money at end of trial': self.bot.money})


    def allocate_money(self):
        # does both the bot and the player start with some?
        self.bot.money = 0
        self.player.money = self.initial_money
        self.log({'money allocated to player': self.initial_money})


    def draw(self, message=''):
        self.player.draw()
        self.bot.draw()

        self.text_stim.text = message
        self.text_stim.draw()

    def draw_transfer(self, to_bot, amount, message=''):
        self.draw(message)
        if to_bot:
            self.right_arrow.draw()
            mes = '+' + str(amount) + ' x 3'
        else:
            self.left_arrow.draw()
            mes = '+' + str(amount)

        self.amount_stim.text = mes
        self.amount_stim.draw()



class PublicGoodsEngine(BaseEngine):
    def __init__(self, win, info, agents, rounds=4):
        BaseEngine.__init__(self, win, info, agents, rounds=rounds)
        self.common_fund = 0


    
    def run_round(self, _=None):
        pass
        # allocate game budget (or round budget?)

        # draw situation, press enter to start turn?
        
        # get moves

        # add money to the pool

        # draw situation (adding money to the pool), press enter to continue

        # draw returning money to agents