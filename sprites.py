from psychopy import visual


class AgentSprite():
    def __init__(self, win, name, pos=(0,0)):
        self.name = name
        self.pos = pos

        self.name_stim = visual.TextStim(win, text=name, units='norm')
        self.ready_stim = visual.TextStim(win, text='READY', color='green', units='norm')
        # self.not_ready_stim = visual.TextStim(win, text='NOT READY', color='red', units='norm')
        self.credit_stim = visual.TextStim(win, text='', units='norm')

        self.highlight = False
        self.disp_ready = False
        self.disp_credits = False
        # self.disp_not_ready = False


        self.update()



    def update(self):
        self.name_stim.pos = self.pos
        self.ready_stim.pos = (self.pos[0], self.pos[1]-.2)
        self.credit_stim.pos = (self.pos[0], self.pos[1]-.1)
        # self.not_ready_stim.pos = (self.pos[0], self.pos[1]-.1)

        if self.highlight:
            self.name_stim.color = 'black'



    def draw(self):
        self.update()

        self.name_stim.draw()
        if self.disp_ready: self.ready_stim.draw()
        if self.disp_credits: self.credit_stim.draw()
        # if self.disp_not_ready: self.not_ready_stim.draw()