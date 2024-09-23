import tkinter as tk
from tkinter.ttk import Combobox, Progressbar
from tkinter import messagebox
import time

app = tk.Tk()
app.title("Test Window")
app.geometry("400x300")

# กรอบที่ 1 Combobox
frame = tk.Frame(app)
frame.pack(fill='x')

def onChange(object):
    print("Value "+str(cbbox.get()))
    
    
def click_select():
    print("Combo : "+str(cbbox.get()))
    data = list_box.curselection() #การเลือกรายการ และเก็บรายการที่เลือกไว้ในตัวแปร data
    if data:
        select_data = list_box.get(data[0])
        print("Food : "+str(select_data)) #list_box.get(data) คือการดึง data มาแสดงผลด้วย method .get()
    else:
        print("Food : No item selected")
    print("Comments : "+str(text_box.get("1.0",tk.END)))
    
# ฟังก์ชันของ progressbar   
# def IncreaseValue():
#     progress['value'] += 1
    
# def DecreaseValue():
#     progress["value"] -= 1

def start_progress():
    progress["value"]=0 # ตั้งค่า progress['value'] = 0
    app.update_idletasks() #การเรียกใช้ update_idletasks() จะช่วยให้ UI แสดงค่าของ Progressbar เป็น 0 ทันที นี่ช่วยให้ผู้ใช้เห็นว่า Progressbar ได้ถูกรีเซ็ตก่อนเริ่มกระบวนการ
    for i in range(101):
        progress["value"] = i
        # คุณกำลังเพิ่มค่าของ Progressbar จาก 0 ถึง 100. การเรียกใช้ update_idletasks() ที่นี่จะทำให้ UI อัปเดตค่าที่แสดงอยู่ ซึ่งช่วยให้ผู้ใช้เห็นการเปลี่ยนแปลงใน Progressbar อย่างต่อเนื่องขณะที่โปรแกรมทำงาน        
        app.update_idletasks() # อัปเดตค่าของ Progressbar ในทุก ๆ รอบของการวนลูป 
        time.sleep(0.1)
        if i == progress["maximum"]:
            messagebox.showinfo("ติดตั้ง","ดาวน์โหลดเสร็จสิ้น")
            
            

lists = [1,2,3,4,5,6,7,8,9]
cbbox = Combobox(frame,values=lists)
cbbox.pack(side="left")
cbbox.current(0)
#cbbox.bind("<<ComboboxSelected>>",onChange)

# Listbox
menu = ['ข้าวผัด','ผัดไทย','ส้มตำ','กะเพราหมูสับ']
list_box = tk.Listbox(frame)
for i in menu:
    list_box.insert(tk.END,i)
list_box.pack(side='left')

# btn = tk.Button(frame,text="Select food",command=onChange)
# btn.pack(side='left')

# ข้อความ
text_box = tk.Text(frame,height=10,width=100)
text_box.pack(side="left",padx=(10,0)) #ขยายวิดเจ็ตในแนวนอน (แนวแกน X) ให้เต็มพื้นที่ที่มีอยู่

btn = tk.Button(frame,text="Add comments",command=click_select)
btn.pack(side='left')

# กรอบที่ 2
frame2 = tk.Frame(app,height=10,width=100)
frame2.pack(fill="x")


# progressbar และ ปุ่มเพิ่มลดค่า
# progress = Progressbar(frame2,length=100)
# progress.pack(side="left")
# progress['value']=50

# btn2 = tk.Button(frame2,text="Increase",command=IncreaseValue)
# btn2.pack(side="left")
# btn3 = tk.Button(frame2,text="Decrease",command=DecreaseValue)
# btn3.pack(side="left")

# สร้าง progressbar ใหม่
progress = Progressbar(frame2,orient='horizontal',length=300,mode='determinate')
progress.pack(pady=20,side="left",padx=(10,0))

progress['maximum'] = 100
progress['value'] = 0

btn_start = tk.Button(frame2,text="Start",width=10,command=start_progress)
btn_start.pack(side="left",padx=(10,0))


app.mainloop()