import tkinter as tk
import time

class pet():
    def __init__(self):
        self.window = tk.Tk()
        #code below generates string for each frame in gif
        self.moveleft = [tk.PhotoImage(file='duck-left.gif', format='gif -index %i' % (i)) for i in range(10)]
        self.moveright = [tk.PhotoImage(file='duck-right.gif', format='gif -index %i' % (i)) for i in range(10)]
        self.frame_index = 0 #setting starting frame
        self.img = self.moveleft[self.frame_index]      #starting direction gif
        self.timestamp = time.time()
        self.window.config(background='black')
        self.window.wm_attributes('-transparentcolor', 'black')
        self.window.overrideredirect(True)      #makes window frameless
        self.window.attributes('-topmost', True)        #puts window on top
        self.label = tk.Label(self.window, bd=0, bg='black')    #creates a label as a container for a gif
        #starting points
        self.x = 1040
        self.y = 670
        self.window.geometry('128x128+{}+{}'.format(str(self.x), str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(0, self.update)
        self.dir = -1   #starting direction
        self.window.mainloop()

    def changetime(self, direction):
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            self.frame_index = (self.frame_index + 1) % 5   #speed of frames change
            self.img = direction[self.frame_index]

    def changedir(self):
        self.dir = -(self.dir)

    def go(self):
        self.x = self.x + self.dir
        if self.dir <0:
            direction = self.moveleft
        else:
            direction = self.moveright
        self.changetime(direction)


    def update(self):
        self.go()
        if self.x == 560 or self.x == 1060:
            self.changedir()

        self.window.geometry('128x128+{}+{}'.format(str(self.x), str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(10, self.update)  #10 is frames number for my gif
        self.window.lift()

pet()