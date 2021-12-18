#info
name = 'PrettyHTML'
version = '1.0.0'
author= 'Filip Rokita'
website = 'www.filiprokita.com'



#import
import tkinter as tk
from bs4 import BeautifulSoup
from tkinter import filedialog
from tkinter import messagebox


#def
def choose():
    global filedir; filedir = filedialog.askopenfilename(title=name, initialdir='./', filetypes=[('html', '*.html')])
    try:
        f = open(filedir, 'r')
        prettyB['state'] = tk.NORMAL
        global data; data = f.read()
        f.close()
    except:
        messagebox.showerror(title=name, message='Choose file!')


def pretty():
    soup = BeautifulSoup(data, 'html.parser')
    prettyfied = soup.prettify()
    f = open(filedir, 'w')
    f.write(prettyfied)
    f.close()



#main
root = tk.Tk()
root.title(name)
root.geometry('300x100')
root.resizable(False, False)


chooseB = tk.Button(root, text='Choose File', command=choose, width=15); chooseB.pack()
prettyB = tk.Button(root, text='Prettify', state=tk.DISABLED, command=pretty, width=15); prettyB.pack(pady=10)
authorL = tk.Label(root, text=website); authorL.pack()


root.mainloop()