from tkinter import *
from tkinter import ttk
 
class Encrypter(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		self.header_label = Label(self, text='Шифратор в операционной системе', font=('Arial', 20))
		self.header_label.pack(anchor='center', fill=X, expand=True)
		
		self.translation_frame = Frame(self)
		self.translation_frame.pack(anchor='center', fill=BOTH, expand=True)
		
		
		self.text = Text(self.translation_frame, height=10, wrap='word')
		self.btn_frame = Frame(self.translation_frame)
		self.btn_encrypt = ttk.Button(self.btn_frame, text='encrypt', command=self._encrypt)
		self.btn_decrypt = ttk.Button(self.btn_frame, text='decrypt', command=self._decrypt)
		self.btn_clear = ttk.Button(self.btn_frame, text='clear', command=self.clear)
		self.translated_text = Text(self.translation_frame, height=10, wrap='word')
		self.text.pack(anchor='center')
		self.btn_frame.pack(anchor='center')
		self.btn_encrypt.grid(row=0, column=0)
		self.btn_decrypt.grid(row=0, column=1)
		self.btn_clear.grid(row=0, column=2)
		self.translated_text.pack(anchor='center')


	def _encrypt(self):
		self.translated_text.delete('1.0', 'end')
		text = self.text.get('1.0', 'end').replace('  ', ' ').strip()
		encrypted = Encrypter.encrypt(text, 42)
		self.translated_text.insert('1.0', encrypted)
		
		
	def _decrypt(self):
		self.translated_text.delete('1.0', 'end')
		text = self.text.get('1.0', 'end').replace('  ', ' ').strip()
		encrypted = Encrypter.decrypt(text, 42)
		self.translated_text.insert('1.0', encrypted)
		
		
	def clear(self):
		self.text.delete('1.0', 'end')
		self.translated_text.delete('1.0', 'end')
		
		
	def encrypt(message, key):
		encrypted = ""
		for char in message:
		    if char.isalpha():
		        if char.islower():
		            encrypted += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
		        else:
		            encrypted += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
		    else:
		        encrypted += char
		return encrypted

	def decrypt(encrypted_message, key):
		decrypted = ""
		for char in encrypted_message:
		    if char.isalpha():
		        if char.islower():
		            decrypted += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
		        else:
		            decrypted += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
		    else:
		        decrypted += char
		return decrypted
