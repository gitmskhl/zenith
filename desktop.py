from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from translator import Translator
from encrypter import Encrypter
from utils import make_draggable, get_photo_image

from settings import *

class Desktop(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		self.controller = controller
		
		self.images_dir = 'images/'
		self.anchors = {}
		self.init_anchors()
		
		background_image = get_photo_image('background.png', (WIDTH, HEIGHT))
		canvas = Canvas(self, width=WIDTH, height=HEIGHT)
		canvas.pack(fill=BOTH, expand=True)
		canvas.background = background_image
		canvas.create_image(0, 0, anchor=NW, image=background_image)
		
		main = canvas
		for icon_label, (icon, class_of_frame) in self.anchors.items():
			label = Label(main, text=icon_label, image=icon, compound='top')
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
		icon_translator = get_photo_image('translator.png', (50, 50))
		self.anchors['translator'] = (icon_translator, Translator)

		icon_encrypter = get_photo_image('encrypter.png', (50, 50))
		self.anchors['encrypter'] = (icon_encrypter, Encrypter)
