import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from tkinter import *
from instabot import Bot
bot = Bot()

def success():
    messagebox.showinfo("Successfully sent the message to @" + my_entry.get())

global send
window = tk.Tk()
window.title("IG - Sender by intel1337")


def send():
    bot.login(username=(my_entry.get()), password=my_entry2.get())
    bot.send_message(my_entryt.get(), [my_entryu.get()])

bouton=Button(window, text="Username :", bg='#5B5B5B')
bouton.pack(side=TOP, padx=50, pady=10)
my_entry = Entry(window, bg='#3E3E3E')
my_entry.pack()

bouton=Button(window, text="Password :", bg='#5B5B5B')
bouton.pack(side=TOP, padx=50, pady=10)
my_entry2 = Entry(window, bg='#3E3E3E')
my_entry2.pack()

bouton=Button(window, text="Message :", bg='#5B5B5B')
bouton.pack(side=TOP, padx=50, pady=10)
my_entryt = Entry(window, bg='#3E3E3E')
my_entryt.pack()

bouton=Button(window, text="Receiver :", bg='#5B5B5B')
bouton.pack(side=TOP, padx=50, pady=10)
my_entryu = Entry(window, bg='#3E3E3E')
my_entryu.pack()


bouton=Button(window, text="Envoyer :", command=send, bg='#00FF0C')
bouton.pack(side=TOP, padx=50, pady=10)


window.iconbitmap('logo.ico')
window.configure(bg='#383838')
window.geometry("300x400")
window.mainloop()


