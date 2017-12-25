import tkinter as tk
from tkinter import ttk

class Spinbox(ttk.Widget):
    def __init__(self, master, **kw):
        ttk.Widget.__init__(self, master, 'ttk::spinbox', kw)

root = tk.Tk()

pad = [3, 5]

ttk.Button(root, text="Button").pack(side="left", padx=pad[0], pady=pad[1])
ttk.Checkbutton(root).pack(side="left", padx=pad[0], pady=pad[1])
Spinbox(root).pack(side="left", padx=pad[0], pady=pad[1])
ttk.Scale(root).pack(side="left", padx=pad[0], pady=pad[1])
ttk.Entry(root).pack(side="left", padx=pad[0], pady=pad[1])
ttk.Radiobutton(root).pack(side="left", padx=pad[0], pady=pad[1])

root.mainloop()
