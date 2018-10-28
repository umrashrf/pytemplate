import bot.globals

import logging.config
logging.config.fileConfig(bot.globals.LOGGING_CONFIG_FILE)

import tkinter as tk

from bot.ui import Application


def main():
    logging.info("Initiating...")
    root = tk.Tk()
    Application(root)
    root.mainloop()
