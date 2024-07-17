import tkinter as Tk

class SliderFrame(Tk.Canvas):
    def __init__(self, parent, callback):
        Tk.Canvas.__init__(self, parent, bg='white')
        self.parent = parent
        self.box = None

        self.slider_state = False
        self.slider_position = 20
        self.values = {'cur': 6.1, 'min': 0.1, 'max': 12.1, 'step': 0.1, 'unit': 'pF'}

        self.callback = callback

        self.snap_pixels = (self.values['max'] - self.values['min']) / self.values['step'] / 400

        self.highvar = Tk.StringVar()
        self.elemvar = Tk.StringVar()
        self.lowvar = Tk.StringVar()

        self.canvas1 = Tk.Canvas(width=200, height=500)
        self.canvas1.configure(background='white')
        self.canvas1.grid(row=1, column=0, stick=Tk.N)

        self.canvas1.create_line(50, 50, 50, 450, width=4, fill='#777')
        self.slider = self.canvas1.create_line(40, 250, 60, 250, width=10, fill='#228')

        self.entry_high = Tk.Entry(self.canvas1, width=6, bg=self.canvas1['bg'], textvariable=self.highvar,
                                   justify='center', state='readonly')
        self.entry_high.bind('<Return>', self.update_slider) # type: ignore

        self.canvas1.create_window(50, 25, window=self.entry_high)
        self.valuetext = self.canvas1.create_text(90, 250, text=self.elemvar.get())
        self.entry_low = Tk.Entry(self.canvas1, width=6, bg=self.canvas1['bg'], textvariable=self.lowvar,
                                  justify='center', state='readonly')
       self.entry_low.bind('<Return>', lambda event: self.update_slider())

        self.canvas1.create_window(50, 475, window=self.entry_low)

        self.canvas1.update()
        self.canvas1.tag_bind(self.slider, '<ButtonPress-1>', self.slideon)
        self.canvas1.bind('<B1-Motion>', self.mouse_move_slider)

        self.update_slider()

def update_slider(self, **kargs):
    pass

def handle_return_event(event):
    self.update_slider()

self.entry_low.bind('<Return>', handle_return_event)

    def update_slider_position(self):
        self.move_slider_value(self.values['cur'])

    def slider_active(self, *args):
        if not self.slider_state:
            self.box = self.canvas1.create_rectangle(35, 45, 65, 455, width=1, dash='.')
            self.slider_state = True

   def slider_deactive(self, *args):
       if self.slider_state and self.box is not None:
           self.canvas1.delete(self.box)
       self.slider_state = False

    def slideon(self, event):
        self.slider_active()
        self.slide_active = True

    def slideoff(self, event):
        self.slider_deactive()
        self.slider_state = False

    def val_from_coord(self, y):
        Vmin = self.values['min']
        Vmax = self.values['max']

        m = (Vmin - Vmax) / (450.0 - 50.0)

        return m * (y - 450.0) + Vmin

    def coord_from_val(self, val):
        Vmin = self.values['min']
        Vmax = self.values['max']

        m = (Vmin - Vmax) / (450.0 - 50.0)

        return (val - Vmin) / m + 450.0

    def mouse_move_slider(self, event):
        new_x, new_y = event.x, event.y
        x1, y1, x2, y2 = self.canvas1.coords(self.slider)

        if 50 <= new_y <= 450:
            distance = new_y - y2
            if abs(distance) >= self.snap_pixels:
                distance = int((new_y - y2) / self.snap_pixels) * self.snap_pixels
                self.canvas1.move(self.slider, 0, distance)
                self.slider_position = y2 + distance

                self.values['cur'] = self.val_from_coord(self.slider_position)

            self.update_slider()

            self.callback(values={'cur': self.values['cur']})

    def move_slider_value(self, val):
        x1, y1, x2, y2 = self.canvas1.coords(self.slider)
        self.values['cur'] = val
        self.canvas1.move(self.slider, 0, self.coord_from_val(val) - y1)


class MainWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)

        # SLIDER FRAME
        Slider_Frame = Tk.Frame(root)
        Slider_Frame.grid(row=0, column=0)

        slider_canvas = Tk.Canvas(Slider_Frame)
        slider = SliderFrame(slider_canvas, self.callback)  # Pass the callback method

    def callback(self, **kargs):
        print("CALLBACK", kargs)  # Modify this function as needed


if __name__ == '__main__':
    root = Tk.Tk()
    a = MainWindow(root)
    root.mainloop()
