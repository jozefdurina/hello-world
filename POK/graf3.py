# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:24:35 2020

@author: Dar0
"""

from tkinter import * #import tkinter module
from visualizer import main #import module 'visualizer' that shows the graph in real time

class Application(Frame):
    ''' Interface for visualizing graphs, indicators and text-box. '''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        # Label of the 1st graph
        Label(self,
              text='Hook Load / Elevator Height / Depth vs Time'
              ).grid(row = 0, column = 0, sticky = W)
        
        # Graph 1 - Hook Load / Elevator Height / Depth vs Time
        # button that displays the plot 
        #plot_button = Button(self,2
        #                     command = main,
        #                     height = 2, 
        #                     width = 10, 
        #                     text = "Plot"
        #                     ).grid(row = 1, column = 0, sticky = W)
        
        self.graph_1 = main(root, 1, 0)
        # place the button 
        # in main window 
        
        # Label of the 2nd graph
        Label(self,
              text = 'Hook Load / Elevator Height vs Time'
              ).grid(row = 3, column = 0, sticky = W)
        
        # Graph 2 - Hook Load / Elevator Height vs Time
        self.graph_2 = main(root, 4, 0)
        
        #Label of the 3rd graph
        Label(self,
              text = 'Hook Load vs Time'
              ).grid(row = 6, column = 0, sticky = W)
        
        #Graph 3 - Hook Load vs Time
        
        #Label of the 1st indicator
        Label(self,
              text = '1st performance indicator'
              ).grid(row = 0, column = 1, sticky = W)
        
        #1st performance indicator
        
        #Label of 2nd performance indicator
        Label(self,
              text = '2nd performance indicator'
              ).grid(row = 3, column = 1, sticky = W)
        
        #2nd performance indicator
        
        #Label of 3rd performance indicator
        Label(self,
              text = '3rd performance indicator'
              ).grid(row = 6, column = 1, sticky = W)
        
        #Text-box showing comments based on received data
        self.text_box = Text(self, width = 50, height = 10, wrap = WORD)
        self.text_box.grid(row = 9, column = 0, columnspan = 1)
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, 'My message will be here.')
        
#Main part
root = Tk()
root.title('WiTSML Visualizer by Dar0')
app = Application(root)
root.mainloop()