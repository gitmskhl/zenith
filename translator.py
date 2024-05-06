from tkinter import *
from tkinter import ttk

import time
import sys
import re

if (sys.version_info[0] < 3):
    import urllib2
    import urllib
    import HTMLParser
else:
    import html
    import urllib.request
    import urllib.parse

agent = {'User-Agent':
         "Mozilla/4.0 (\
compatible;\
MSIE 6.0;\
Windows NT 5.1;\
SV1;\
.NET CLR 1.1.4322;\
.NET CLR 2.0.50727;\
.NET CLR 3.0.04506.30\
)"}


class Translator(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		self.controller = controller
		self.header_label = Label(self, text='Переводчик в операционной системе', font=('Arial', 20))
		self.header_label.pack(anchor='center', fill=X, expand=True)
		
		self.translation_frame = Frame(self)
		self.translation_frame.pack(anchor='center', fill=BOTH, expand=True)
		
		
		self.text = Text(self.translation_frame, height=10, wrap='word')
		self.btn_frame = Frame(self.translation_frame)
		self.btn_translate = ttk.Button(self.btn_frame, text='translate', command=lambda: self._translate_text())
		self.btn_clear = ttk.Button(self.btn_frame, text='clear', command=lambda: self._clear_text())
		self.translated_text = Text(self.translation_frame, height=10, wrap='word')
		self.text.pack(anchor='center')
		self.btn_frame.pack(anchor='center')
		self.btn_translate.grid(row=0, column=0)
		self.btn_clear.grid(row=0, column=1)
		self.translated_text.pack(anchor='center')
		
		
	def _clear_text(self):
		self.text.delete('1.0', 'end')
		self.translated_text.delete('1.0', 'end')
		
		
	def _translate_text(self):
		self.translated_text.delete('1.0', 'end')
		text = self.text.get('1.0', 'end').replace('  ', ' ').strip()
		translated_text = translate(text)
		self.translated_text.insert('1.0', translated_text)
		
		



def unescape(text):
    if (sys.version_info[0] < 3):
        parser = HTMLParser.HTMLParser()
    else:
        parser = html
    return (parser.unescape(text))


def translate1(to_translate, to_language="auto", from_language="auto"):
    """Returns the translation using google translate
    you must shortcut the language you define
    (French = fr, English = en, Spanish = es, etc...)
    if not defined it will detect it or use english by default

    Example:
    print(translate("salut tu vas bien?", "en"))
    hello you alright?
    """
    base_link = "http://translate.google.com/m?tl=%s&sl=%s&q=%s"
    if (sys.version_info[0] < 3):
        to_translate = urllib.quote_plus(to_translate)
        link = base_link % (to_language, from_language, to_translate)
        request = urllib2.Request(link, headers=agent)
        raw_data = urllib2.urlopen(request).read()
    else:
        to_translate = urllib.parse.quote(to_translate)
        link = base_link % (to_language, from_language, to_translate)
        request = urllib.request.Request(link, headers=agent)
        raw_data = urllib.request.urlopen(request).read()
    data = raw_data.decode("utf-8")
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    re_result = re.findall(expr, data)
    if (len(re_result) == 0):
        result = ""
    else:
        result = unescape(re_result[0])
    return (result)
    
    
def translate(text):
	en = "abcdefghijklmnopqrstuvwxyz"
	text = text.lower()
	text = text.strip()
	to = "en"
	if text[0] in en or text[1] in en:
		to = "ru"
	return translate1(text, to)
	
