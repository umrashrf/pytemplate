from tkinter import (
    Frame,
    Button,
)


class Application(Frame):

    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        close = Button(self)
        close["text"] = "Close"
        close["fg"]   = "red"
        close["command"] =  self.quit
        close["width"] = 25

        close.pack({"side": "bottom"})

        hi_there = Button(self)
        hi_there["text"] = "Hello",
        hi_there["command"] = self.say_hi
        hi_there["width"] = 25

        hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
