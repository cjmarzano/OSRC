# gui.py

# Gui.pi contains all code pertaining to the GUI. This includes updating the screen and
# handling all events raised by the user through the touchpad.

# Import from packages
from tkinter import *
from PIL import Image, ImageTk

# Import from files
from config import * # This makes me feel dirty
import timing

class Main_Window(Frame):
  
	def __init__(self, parent):
		Frame.__init__(self, parent, background="white")   
		self.parent = parent
		self.initUI()

	def initUI(self):
	# Set up the window
		self.parent.title("OSRC")
		self.pack(fill=BOTH, expand=1)
	# Center window on screen
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - screenwidth)/2
		y = (sh - screenheight)/2
		self.parent.geometry('%dx%d+%d+%d' % (screenwidth, screenheight, x, y))
	# Load background image
		self.img = Image.open(backgroundimage)
		self.background = ImageTk.PhotoImage(self.img)
		canvas = Canvas(self, width=backgroundcanvaswidth, 
			height=backgroundcanvasheight)
		canvas.create_image(screenwidth/2, screenheight/2, anchor=CENTER, image=self.background)
		canvas.pack(fill=BOTH, expand=1)
		
def tick(time1=''):
	# get the current local time from the PC
	time2 = timing.formattedtime()
	# if time string has changed, update it
	if time2 != time1:
		time1 = time2
		clock.config(text=time2)
	# calls itself every 200 milliseconds
	# to update the time display as needed
	clock.after(200, tick)	

root = Tk()	
clock = Label(root, font=('times', 20, 'bold'), bg='white')
clock.pack(fill=BOTH, expand=1)
	
def main():
	app = Main_Window(root)
	tick()
	root.mainloop()  
	
if __name__ == '__main__':
	main()