import tkinter as tk
import time


class Clock(tk.Tk):
    def __init__(self):
        super(Clock, self).__init__()
        self.overrideredirect(True)
        self.window_size = '320x80'
        self.geometry(self.window_size + '+400+200')

        self.x = 0
        self.y = 0
        self.movable = True

        self.show_label = None

        self.load_widget()
        self.bind_event()

    def load_widget(self):
        self.show_label = tk.Label(self, font=('calibri', 40, 'bold'),background='Black',foreground='white')
        self.show_label.pack(expand=True, fill='both')
        self.show_label.bind('<Button-3>', self.post)
        self.time()

    def post(self, event):
        menu = tk.Menu(self, tearoff=0)
        menu.add_cascade(label='红色', command=lambda: self.color('red'))
        menu.add_cascade(label='黑色', command=lambda: self.color('black'))
        menu.add_cascade(label='黄色', command=lambda: self.color('yellow'))
        menu.add_cascade(label='蓝色', command=lambda: self.color('blue'))
        menu.post(event.x_root, event.y_root)

    def color(self, color):
        self.show_label.config(bg=color)

    def time(self):
        string = time.strftime('%H:%M:%S %p')
        self.show_label.config(text=string)
        self.show_label.after(1000, self.time)

    def bind_event(self):
        self.bind('<Button-1>', self.button_down)       # 左键按下
        self.bind('<ButtonRelease-1>', self.button_up)  # 左键松开
        self.bind('<B1-Motion>', self.button_move)      # 左键按下并移动

    def button_down(self, event):
        self.x = event.x
        self.y = event.y
        self.movable = True

    def button_up(self, event):
        self.movable = False

    def button_move(self, event):
        if self.movable:
            x = self.winfo_x() + (event.x - self.x)
            y = self.winfo_y() + (event.y - self.y)
            self.geometry(f'{self.window_size}+{x}+{y}')


c = Clock()
c.mainloop()

