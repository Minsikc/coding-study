from tkinter import*
import requests

from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

    def get_img(self):

        load = Image.open("index.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


root = Tk()
app = Window(root)
button = Button(root, text="Get Image", font=10, command = lambda: app.get_img())
button.place(relx=0.3, rely = 0.8)


root.wm_title("Tkinter window")
root.geometry("300x300")

root.mainloop()

