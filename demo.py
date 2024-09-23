import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox


app = tk.Tk()
app.title("Multitask")
app.geometry("500x700")

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

items = tk.StringVar()
tools = ['C','C++','C#','Python','Dart','Javascript']
combo_box = Combobox(app,values=tools,textvariable=items)
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

def selected():
    data1 = text_box.get("1.0",tk.END).strip() #เก็บข้อความตั้งแต่อักขระแรกจนถึงอันสุดท้ายและเก็บไว้ที่ตัวแปร data
    data2 = items.get()
    data_list = list_box.curselection() # .curselection() คือ การเลือก
    data3 = list_box.get(data_list)
    empty_text.config(text=f"Name: {data1}\nYour language: {data2}\nLibrary: {data3}") #แสดงข้อความในempty_text
    
btn = tk.Button(app,text="Select",command=selected)
btn.pack(pady=(10,0))

# พื้นที่การแสดงข้อความที่พิมพ์ลงไปใน text box
empty_text = tk.Label(app)
empty_text.pack(pady=(10,0))

app.mainloop()