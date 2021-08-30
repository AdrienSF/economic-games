from game_engines import InvestmentGameEngine
from player import InvestmentPlayer
from bots import InvestmentBot

from psychopy import visual, event, core

win = visual.Window(monitor='testMonitor', fullscr=True, color='grey', units='norm')
s = visual.TextStim(win, text='BRUH', color='white', units='norm', pos=(0,.5))
s.draw()
win.flip()
s.draw()
win.flip()

# print(event.waitKeys())

info = {'session_id':666}

engine = InvestmentGameEngine(win, info, player=InvestmentPlayer(win, name='yeehaw'), bot=InvestmentBot(win, name='totaly human player'), rounds=3)


engine.run()

win.close()
# core.quit()