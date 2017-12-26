import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from pprint import pprint

# The TTK wrapper lacks a Spinbox for some reason.
# This provides a wrapped class for it.
class ttk_Spinbox(ttk.Widget):
    def __init__(self, master, **kw):
        ttk.Widget.__init__(self, master, 'ttk::spinbox', kw)

root = tk.Tk()
root.wm_attributes("-topmost", True)
root.geometry("600x80")

pad = [3, 5]

# Create the widgets.
button = ttk.Button(root, text="Button")
button.pack(side="left", padx=pad[0], pady=pad[1])

check = ttk.Checkbutton(root)
check.pack(side="left", padx=pad[0], pady=pad[1])

spin = ttk_Spinbox(root)
spin.pack(side="left", padx=pad[0], pady=pad[1])

scale = ttk.Scale(root)
scale.pack(side="left", padx=pad[0], pady=pad[1])

entry = ttk.Entry(root)
entry.pack(side="left", padx=pad[0], pady=pad[1])

radio = ttk.Radiobutton(root)
radio.pack(side="left", padx=pad[0], pady=pad[1])

scroll = ttk.Scrollbar(root)
scroll.pack(side="left", fill="y", padx=pad[0], pady=pad[1])

text = tk.Text(root, yscrollcommand=scroll.set)
for _ in range(50):
    text.insert("end", "\n")

scroll.configure(command=text.yview)

# Print the layout of the default styles.
pprint(ttk.Style().layout("TButton"))
print()
pprint(ttk.Style().layout("TCheckbutton"))
print()
pprint(ttk.Style().layout("TSpinbox"))
print()
pprint(ttk.Style().layout("Horizontal.TScale"))
print()
pprint(ttk.Style().layout("TEntry"))
print()
pprint(ttk.Style().layout("TRadiobutton"))
print()
pprint(ttk.Style().layout("Horizontal.TScrollbar"))
print()

# Print the system font.
print(tkFont.nametofont("TkDefaultFont").actual())

root.mainloop()
