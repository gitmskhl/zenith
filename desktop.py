from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from translator import Translator
from encrypter import Encrypter
from utils import make_draggable

class Desktop(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		self.controller = controller
		
		self.images_dir = 'images/'
		self.anchors = {}
		self.init_anchors()
		
		self.main_frame = Frame(self)
		self.main_frame.pack(fill=BOTH, expand=True)
		for icon_label, (icon, class_of_frame) in self.anchors.items():
			label = Label(self.main_frame, text=icon_label, image=icon, compound='top')
			label.bind('<Enter>', lambda ev, label=label: self._enter_callback(label))
			label.bind('<Leave>', lambda ev, label=label: self._leave_callback(label))
			label.bind('<Double-Button-1>', lambda ev, class_of_frame=class_of_frame: self._set_as_main_callback(class_of_frame))
			label.pack(anchor='nw')
			make_draggable(label)
		
		self.default_color = label['bg']
		
	
	def _enter_callback(self, obj):
		obj['background'] = 'blue'
		
	def _leave_callback(self, obj):
		obj['background'] = self.default_color#'#F0F0F0'
		
	def _set_as_main_callback(self, class_of_frame):
		self.controller.change_main_frame(class_of_frame)
	
	def init_anchors(self):
		img_translator = Image.open(os.path.join(self.images_dir, 'translator.png')).resize((50, 50))
		icon_translator = ImageTk.PhotoImage(img_translator)
		self.anchors['translator'] = (icon_translator, Translator)

		img_encrypter = Image.open(os.path.join(self.images_dir, 'encrypter.png')).resize((50, 50))
		icon_encrypter = ImageTk.PhotoImage(img_encrypter)
		self.anchors['encrypter'] = (icon_encrypter, Encrypter)
