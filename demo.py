import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox


app = tk.Tk()
app.title("Multitask")
app.geometry("500x500")

# textbox
header = tk.Label(app,text="What happened ?")
header.pack()

text_box = tk.Text(app,width=30,height=10)
text_box.pack()

sub_head = tk.Label(app,text="Comments")
sub_head.pack()

# Combobox
header2 = tk.Label(app,text="Select your state")
header2.pack(pady=(10,0))

tools = ['C','C++','C#','Python','Dart','Javascript']
combo_box = Combobox(app,values=tools)
combo_box.pack()
combo_box.current(0) # ตั้งค่าเริ่มต้นเป็นตัวเลือกแรก

# Listbox
header3 = tk.Label(app,text="Select your library")
header3.pack(pady=(10,0))

libraries = ['Flutter','Tkinter','Bootstrap','Tailwind','Node','Nuxt']
list_box = tk.Listbox(app,selectmode='single') # multiple
for i in libraries:
    list_box.insert(tk.END,i)
list_box.pack()


app.mainloop()