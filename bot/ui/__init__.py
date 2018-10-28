import io
import subprocess

from tkinter import (
    Frame,
    Button,
)


class Application(Frame):

    def say_hi(self):
        cmd = 'python -m bot hello'
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
            print(line)

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
