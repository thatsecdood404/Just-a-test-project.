Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
================================ RESTART: Shell ================================
>>> 
>>> import tkinter as tk
>>>  
class Win1:
	def __init__(self, master):
		self.master = master
		self.master.geometry("400x400")
		self.frame = tk.Frame(self.master)
		self.butnew("Click to open Window 2", "2", Win2)
		self.butnew("Click to open Window 3", "3", Win3)
		self.frame.pack()
 
	def butnew(self, text, number, _class):
		tk.Button(self.frame, text = text, command= lambda: self.new_window(number, _class)).pack()
 
	def new_window(self, number, _class):
		self.new = tk.Toplevel(self.master)
		_class(self.new, number)
		