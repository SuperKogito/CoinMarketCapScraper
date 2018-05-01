# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 02:17:24 2017
@author: SuperKogito
"""
# Define imports
import tkinter as tk
from scrape import Scraper
from tkinter import ttk, Label, Entry, LabelFrame

class MainWindow(tk.Tk):
    """ Main window class """
    def __init__(self, title):
        super().__init__()
        xyla = [0, 0, 1270, 80]
        self.ext = ''
        self.original_path = ''
        self.title(title)
        self.minsize(xyla[2], xyla[3])
        #self.resizable(0, 0)
        self.configure(background='black')
        self.geometry("%dx%d+%d+%d" % (xyla[0], xyla[1], 400, 100))
        # Define bind events
        self.bind("<Escape>", self.quit_func)
        # Define colors
        colors = ["#0080ff", "white", "black"]
        # Define style
        ttk.Style().configure("TNotebook", background=colors[2])
        ttk.Style().map("TNotebook.Tab",
                        background=[("selected", colors[0])],
                        foreground=[("selected", colors[1])])
        
        self.option_add("*Font", "courier")
        self.frame = LabelFrame(self, text="", bg="black", fg='white')
        self.label_frame = tk.Frame(self.frame, bg="black")
        self.input_frame = tk.Frame(self.frame, bg="black")
        
        self.frame.pack(expand=1, fill="both", padx=5, pady=5)
        self.label_frame.pack(expand=1, fill="both", padx=5, pady=2)
        self.input_frame.pack(expand=1, fill="both", padx=10, pady=2)
        
        self.label = Label(self.label_frame, bg="black", fg='white',
                           text='Coinmarketcap historical data URL to scrape from: (example:https://coinmarketcap.com/currencies/bitcoin/historical-data/...)')
        self.entry = Entry(self.input_frame, width=110)
        self.label.pack(side=tk.LEFT)
        self.entry.pack(side=tk.LEFT)
        
        b2 = tk.Button(self.input_frame, text='Scrape', command=self.get_input)
        b2.pack(side=tk.RIGHT, pady=5)
        b2.configure(background="black", foreground='white',
                     activebackground='#0080ff', activeforeground='white')
        
        self.create_menu()
        self.mainloop()

    def create_menu(self):
        self.menu = tk.Menu(self, tearoff=False)
        # Menu item File
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", underline=0, menu=self.filemenu)
        self.filemenu.add_command(label="Exit", underline=2,
                                  command=self.quit_func, accelerator="Esc")
        # Menu item Edit
        self.editmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", underline=0, menu=self.editmenu)
        self.editmenu.add_command(label="Clear", underline=2,
                                  command=self.edit_clear)
        # Coloring the menu
        for menu_element in (self.filemenu, self.editmenu):
            menu_element.configure(bg='black', fg='white',
                                   activebackground='#0080ff',
                                   activeforeground='white')
        self.config(menu=self.menu)
        self.menu.configure(background='black', foreground='white',
                            activebackground='#0080ff',
                            activeforeground='white')

    def quit_func(self, event=None):
        self.destroy()

    # Edit menu functions
    def edit_clear(self, event=None):
        self.entry.delete(0, 'end')

    def get_input(self):
        self.url = self.entry.get()
        print('Scraping from: ', self.url)
        scraper = Scraper()
        data = scraper.process(self.url)
        scraper.write_to_csv(data)
        print('Done.')
        return
