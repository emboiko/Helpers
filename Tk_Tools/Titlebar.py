from tkinter import Frame, Label, Button

class Titlebar:
    def __init__(self, root, title="Titlebar"):
        self.title = title
        self.root = root
        self.root.update()
        self.geometry = self.root.wm_geometry()

        #Widgets:
        self.bar = Frame(self.root, bg="blue")
        self.body = Frame(self.root, bg="red")

        self.label = Label(self.bar, text=self.title)
        self.close_btn = Button(self.bar, text="X", command=self.root.destroy)
        self.max_btn = Button(self.bar, text="[]")
        self.min_btn = Button(self.bar, text="_")

        #Layout
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.bar.columnconfigure(0, weight=1)

        self.bar.grid(row=0, column=0, sticky="new")
        self.body.grid(row=1, column=0, sticky="nsew")

        self.label.grid(row=0, column=0, sticky="w")
        self.min_btn.grid(row=0, column=1)
        self.max_btn.grid(row=0, column=2)
        self.close_btn.grid(row=0, column=3)

        # Geometry / Bindings
        self.delta_x, self.delta_y = 0, 0

        self.bar.bind("<Button-1>", self.get_position)
        self.bar.bind("<B1-Motion>", self.move_window)

        self.titlebar()


    def titlebar(self):
        self.root.overrideredirect(True)
        self.root.geometry(self.geometry)


    def get_position(self, event):
        window_x = self.root.winfo_x()
        window_y = self.root.winfo_y()

        cursor_x = event.x_root
        cursor_y = event.y_root

        self.delta_x = cursor_x - window_x
        self.delta_y = cursor_y - window_y


    def move_window(self, event):
        self.root.geometry(
            f"+{event.x_root - self.delta_x}+{event.y_root - self.delta_y}"
        )
