import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
    
def start():
    artical = misa.get('1.0','end')
    if len(artical) <= 1:
        tk.messagebox.showwarning('给小杰先生的提醒','小杰先生，您还什么都没输入呢')
    else:
        artical = artical.replace('Misa Liu', 'Misa')
        artical = artical.replace('Misa','|')
        artical = artical.replace('小杰','Misa')
        artical = artical.replace('|','小杰')
        xiaojie.config(state='normal')
        xiaojie.delete(1.0, 'end')
        xiaojie.insert('end', artical)
        xiaojie.config(state='disabled')

window = tk.Tk()
window.title("Mr.小杰的文案生成器")
window.geometry("700x600")
window.resizable(0,0)
tk.Label(window, text="Mr.小杰的文案生成器", font=('微软雅黑', 25)).pack()
tk.Label(window, text="请小杰先生在此输入带恶人Misa的文案",font=('微软雅黑', 15)).pack()
misa = scrolledtext.ScrolledText(window, height=10, font=('Simsong', 13))
misa.pack()
tk.Label(window, text="这是为尊敬的小杰先生生成的全新文案",font=('微软雅黑', 15)).pack()
xiaojie = scrolledtext.ScrolledText(window, height=10, font=('Simsong', 13))
xiaojie.pack()
startButton = tk.Button(window, text="生成", height=1, width=20, relief='groove', bg='#dddddd', font=('微软雅黑', 17), command=start).pack()
tk.Label(window, text="Code by rpONE\n欢迎小杰先生联系").pack(side="right")
xiaojie.config(state='disabled')

window.mainloop()