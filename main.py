from tkinter import *
from tkinter import ttk

from translator import Translator
from desktop import Desktop
from encrypter import Encrypter

class MainApp(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		container = Frame(self)
		container.pack(fill=BOTH, expand=True)
		
		container.rowconfigure(0, weight=1)
		container.columnconfigure(0, weight=1)
		
		self.frames = {}

		for F in (Desktop, Translator, Encrypter):
			frame = F(container, self)
			frame['borderwidth'] = 1
			frame['relief'] = 'raised'
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')
		self.change_main_frame(Desktop)
		
		self.btn_desktop = Button(container, text='Desktop', command=self.change_to_desktop)
		self.btn_desktop.grid(row=1, column=0, sticky='nsw')#pack(anchor='sw', expand=True)

	def change_to_desktop(self):
		self.frames[Desktop].tkraise()
		
	def change_main_frame(self, class_of_frame):
		self.frames[class_of_frame].tkraise()







app = MainApp()
app.mainloop()
