import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox


app = tk.Tk()
app.title("Multitask")
app.geometry("500x700")

# กรอบเนื้อหา
frame = tk.Frame(app)
frame.pack(fill='both')

# textbox
header = tk.Label(frame,text="What happened ?")
header.pack(pady=(20,10))

text_box = tk.Text(frame,width=30,height=10)
text_box.pack()

# Combobox
header2 = tk.Label(frame,text="Select your state")
header2.pack(pady=(10,0))

items = tk.StringVar()
tools = ['C','C++','C#','Python','Dart','Javascript']
combo_box = Combobox(frame,values=tools,textvariable=items)
combo_box.pack()
combo_box.current(0) # ตั้งค่าเริ่มต้นเป็นตัวเลือกแรก

# Listbox
header3 = tk.Label(frame,text="Select your library")
header3.pack(pady=(10,0))

libraries = ['Flutter','Tkinter','Bootstrap','Tailwind','Node','Nuxt']
list_box = tk.Listbox(frame,selectmode='single') # multiple
for i in libraries:
    list_box.insert(tk.END,i)
list_box.pack()

def selected():
    data1 = text_box.get("1.0",tk.END).strip() #เก็บข้อความตั้งแต่อักขระแรกจนถึงอันสุดท้ายและเก็บไว้ที่ตัวแปร data
    data2 = items.get()
    data_list = list_box.curselection() # .curselection() คือ การเลือก
    data3 = list_box.get(data_list)
    empty_text.config(text=f"Name: {data1}\nYour language: {data2}\nLibrary: {data3}") #แสดงข้อความในempty_text
    
btn = tk.Button(frame,text="Select",command=selected)
btn.pack(side='bottom')

# พื้นที่การแสดงข้อความที่พิมพ์ลงไปใน text box
empty_text = tk.Label(frame)
empty_text.pack(pady=(10,0))

app.mainloop()